import boto3
from dativa.tools.aws import S3Client
from dativa.tools.aws import TaskQueue
import logging
from os import path
import time
import re
import pandas as pd
logger = logging.getLogger("dativa.tools.aws")


class S3Csv2ParquetConversionError(Exception):
    """
    A generic class for reporting errors in the athena client
    """

    def __init__(self, reason):
        Exception.__init__(self, ' S3Csv2ParquetConversion failed: reason {}'.format(reason))
        self.reason = reason


class S3Csv2Parquet(TaskQueue):
    """
    This class contains functionality to convert csv files to parquet using glue jobs.
    """

    def __init__(self, region, template_location, max_jobs=5,
                 glue_role='AWSGlueServiceRoleDefault', retry_limit=3):
        """
        ## Parameters
        - region - AWS region in which glue job is to be run
        - template_location - S3 bucket Folder in which template scripts are
                              located or need to be copied
        - glue_role - Name of the glue role which need to be assigned to the
                      Glue Job
        - max_jobs - Maximum number of jobs the can run concurrently in the queue
        - retry_limit - Maximum number of retries allowed per job on failure
        """
        super(S3Csv2Parquet, self).__init__(max_jobs, retry_limit)
        self.glue = boto3.client(service_name='glue', region_name=region,
                                 endpoint_url='https://glue.{}.amazonaws.com'.format(region))
        self.max_jobs = max_jobs
        self.glue_role = glue_role
        self.template_location = template_location
        self.s3_client = S3Client()
        # Copy template files to s3
        self._upload_template()

    def convert(self, csv_path, output_folder=None, schema=[], name="parquet_csv_convert",
                allocated_capacity=2, delete_csv=False, separator=",",
                withHeader=1, compression=None, partition_by=None, mode='append'):
        """
        Create a job in glue.

        ## Parameters
        - csv_path - s3 location of the csv file
                     format s3://bucketname/folder/file.csv
        - output_folder - s3 location at which paraquet file should be copied
                         format s3://bucketname/folder
                         If not specified converted files are copied to the same path
                         as csv files
        - schema - If not specified scema is inferred from the file
                   format [(column1, datatype), (column2, datatype)]
                   Supported datatypes are boolean, double, float, integer,
                   long, null, short, string
        - name - Name to be assigned to glue job
        - allocated_capacity - The number of AWS Glue data processing units (DPUs) to allocate to this Job.
                               From 2 to 100 DPUs can be allocated; the default is 10
        - delete_csv - If set source csv files are deleted post successful completion of job
        - separator - Delimiter character in csv files
        - withHeader- Specifies whether to treat the first line as a header
        - compression - If not specified compression is not applied.
                        Can take values snappy, gzip, and lzo
        - partition_by - List containing columns to partition data by
        - mode - Options include:
                 append: Append contents of this DataFrame to existing data.
                 overwrite: Overwrite existing data.
                 error: Throw an exception if data already exists.
                 ignore: Silently ignore this operation if data already exists.
                 Default mode is append
        """

        """ if mapping information is not provided then it will be inferred
            from the first file in the csv list"""

        if isinstance(csv_path, str):
            csv_path = [csv_path]

        self._validate_parameter(csv_path, output_folder, schema,
                                 allocated_capacity, withHeader, delete_csv,
                                 compression, partition_by, mode, separator)

        logger.info("Adding job {} to queue ".format(name))
        myJob = self.add_task({'name': name, 'role': self.glue_role,
                               'command': {'Name': 'glueetl',
                                           'ScriptLocation': path.join(self.template_location,
                                                                       'csv_parquet_template.py')},
                               'allocated_capacity': allocated_capacity,
                               'csv_path': csv_path,
                               'output_folder': output_folder,
                               'schema': schema,
                               'delete_csv': delete_csv,
                               'separator': separator,
                               'withHeader': withHeader,
                               'execution_property': {'MaxConcurrentRuns': min(self.max_jobs, 3)},
                               'compression': compression,
                               'partition_by': partition_by,
                               'mode': mode
                               })

        return myJob

    def _trigger_task(self, task):
        """
        This method creates/updates a job in glue and triggers its execution
        """
        try:
            job_list = self.glue.get_jobs()["Jobs"]
        # If Job with same name exists it is updated else we create a new job
            for job in job_list:
                if job['Name'] == task.arguments['name']:
                    logging.info("Updating job {}".format(task.arguments['name']))
                    self.glue.update_job(JobName=task.arguments['name'],
                                         JobUpdate={"Role": task.arguments['role'],
                                                    "Command": task.arguments['command'],
                                                    "AllocatedCapacity": task.arguments['allocated_capacity'],
                                                    "ExecutionProperty": task.arguments['execution_property']})
                    break
            else:
                logging.info("Creating new job job {}".format(task.arguments['name']))
                self.glue.create_job(Name=task.arguments['name'],
                                     Role=task.arguments['role'], Command=task.arguments['command'],
                                     AllocatedCapacity=task.arguments['allocated_capacity'],
                                     ExecutionProperty=task.arguments['execution_property'])
        except self.glue.exceptions.AccessDeniedException as e:
            logging.error("Failed to create/update job due to -{}".format(e.args[0]))
            raise e
        """
        Calls to the startjobrun api sometime returns ConcurrentRunsExceededException exception
        although active queue contains less that 3 tasks associated with a single job.
        In case ConcurrentRunsExceededException we retry calling startjobrun API
        """
        while True:
            try:
                task.id = self.glue.start_job_run(JobName=task.arguments['name'],
                                                  Arguments={'--csv_path': str(task.arguments['csv_path']).replace(' ', ''),
                                                             '--output_folder': str(task.arguments['output_folder']),
                                                             '--schema': str(task.arguments['schema']).replace(' ', ''),
                                                             '--separator': task.arguments['separator'],
                                                             '--withHeader': str(task.arguments['withHeader']),
                                                             '--compression': str(task.arguments['compression']),
                                                             '--partitionBy': str(task.arguments['partition_by']),
                                                             '--mode': task.arguments['mode']})['JobRunId']
                logger.info("Execution of Job {} has started".format(task.arguments['name']))
                task.is_active = True
                break
            except self.glue.exceptions.ConcurrentRunsExceededException:
                logger.info("Attempt to run job raised ConcurrentRunsExceededException")
                logger.info("Will reattempt to start job in 30 secs")
                time.sleep(30)

    def _update_task_status(self, task):
        """
        Gets the status of the query, and updates its status in the queue.
        Any queries that fail are reset to pending so they will be run a second time
        """

        logger.info("...checking status of job {0}".format(task.arguments['name']))
        status = self.glue.get_job_run(JobName=task.arguments['name'],
                                       RunId=task.id)['JobRun']['JobRunState']
        if status == "RUNNING":
            task.is_active = True
        elif status == "SUCCEEDED":
            task.is_active = False
            if task.arguments['delete_csv']:
                for each_file in task.arguments['csv_path']:
                    s3_bucket = each_file.split("/")[2]
                    file_path = "/".join(each_file.split("/")[3:])
                    self.s3_client.delete_files(s3_bucket, file_path)
        elif task.retries < self.retry_limit:
            logger.info("Retrying job {0} completed with state {1}".
                        format(task.arguments['name'], status))
            task.retries += 1
            task.is_active = True
        else:
            logger.info("job with Name {} and id {} has exceeded retry_limit\
                        and has been marked as failed".
                        format(task.arguments['name'], task.id))
            task.is_active = False
        return task

    def _upload_template(self):
        """
        Upload template files to s3 if they have been changed
        """

        s3_bucket = self.template_location.split("/")[2]
        template_path = "/".join(self.template_location.split("/")[3:])
        template_file_local = path.join(path.dirname(path.abspath(__file__)),
                                        "template_scripts")
        key_list = boto3.client("s3").list_objects(Bucket=s3_bucket,
                                                   Prefix=path.join(template_path,
                                                                    "csv_parquet_template.py"))

        """ Check if template file is available in s3 and size matches with the
            one present in dativa tools package"""
        if ("Contents" not in key_list.keys()) or \
           (key_list['Contents'][0]['Size'] != path.getsize(template_file_local)):
            local_template_path = path.join(path.dirname(path.abspath(__file__)), "template_scripts")
            self.s3_client.put_folder(local_template_path, s3_bucket, template_path)

    def _running_jobs(self, job_name):
        """
        Return the number of concurrent jobs
        """
        running_jobs = 0
        for each_job in self.active_queue:
            if each_job.arguments['name'] == job_name:
                running_jobs += 1
        return running_jobs

    def _fill_active_queue(self):
        """
        Removes completed task from active queue and populates freed spots with tasks
        in the front of pending_tasks queue
        """
        for i in range(0, self.max_size - len(self.active_queue)):
            if not(self.pending_tasks.empty()):
                task = self.pending_tasks.get()

                """
                Glue does not allow more than 3 concurrent executions of a job.
                The while loop ensures that the active queue does not contain
                more than 3 tasks that belong to the same job
                """
                while True:
                    if self._running_jobs(task.arguments['name']) > 2:
                        logger.info("There are 3 concurrent runs of job: {}".format(task.arguments['name']))
                        logger.info("Waiting for these jobs to complete before adding them to active list")
                        time.sleep(30)
                        self._empty_active_queue()
                    else:
                        self.active_queue.append(task)
                        self._trigger_task(task)
                        break
            else:
                break

    def _validate_parameter(self, csv_path, output_folder, schema,
                            allocated_capacity, withHeader, delete_csv,
                            compression, partition_by, mode, separator):
        """
        This method validates if parameters passed to the convert method
        are correct.
        """

        s3_file_pattern = re.compile("s3://.")

        for each_file in csv_path:
            if s3_file_pattern.match(each_file) is None:
                logging.error("csv_path-{} is not of format \
                              s3://bucketname/folder".format(each_file))
                raise S3Csv2ParquetConversionError("csv_path-{} is not of \
                                                   format s3://bucketname/folder".format(each_file))

        if not isinstance(output_folder, str) and output_folder is not None:
            logging.error("output_folder must be of type string got {} instead".format(str(type(output_folder))))
            raise S3Csv2ParquetConversionError("output_folder must be of type string got {} instead".
                                               format(str(type(output_folder))))
        if output_folder is not None and len(output_folder) and s3_file_pattern.match(output_folder) is None:
            logging.error("output_folder-{} is not of format \
                          s3://bucketname/folder".format(output_folder))
            raise S3Csv2ParquetConversionError("output_folder-{} is not of \
                                               format s3://bucketname/folder".
                                               format(output_folder))

        if not isinstance(schema, list):
            logging.error("schema parameter must be of format '[('column1', 'datatype')]'")
            raise S3Csv2ParquetConversionError("schema parameter must be of format '[('column1', 'datatype')]'")

        supported_datatypes = ['boolean', 'double', 'float', 'integer', 'long', 'null', 'short', 'string']
        for each_pair in schema:
            if each_pair[1].lower() not in supported_datatypes:
                logging.error("Datatypes listed in schema must be one of the following {}".
                              format(",".join(supported_datatypes)))
                logging.error("{} is not supported".format(each_pair[1]))
                raise S3Csv2ParquetConversionError("Datatypes listed in schema must be one of the following {}".
                                                   format(",".join(supported_datatypes)))

        if allocated_capacity > 100 or allocated_capacity < 2:
            logging.error("allocated capacity should be in range 2-100")
            raise S3Csv2ParquetConversionError("allocated capacity should be in range 2-100")

        if withHeader not in [0, 1]:
            logging.error("{} is not a valid value for withHeader it can only \
                          take interger values 1 and 0".format(withHeader))
            raise S3Csv2ParquetConversionError("{} is not a valid value for \
                                               withHeader it can only take \
                                               interger values 1 and 0".format(withHeader))

        if not isinstance(delete_csv, bool):
            logging.error("{} is not a valid value for delete_csv.\
                          It can only take boolean values")
            raise S3Csv2ParquetConversionError("{} is not a valid value for delete_csv.\
                          It can only take boolean values")

        compression_methods = ['snappy', 'gzip', 'lzo']
        if compression is not None and compression not in compression_methods:
            logging.error("Compression must be of type {}".
                          format(",".join(compression_methods)))
            raise S3Csv2ParquetConversionError("Compression must be of type {}".
                                               format(",".join(compression_methods)))

        if not isinstance(partition_by, list) and partition_by is not None:
            logging.error("partition_by parameter must be of type list")
            raise S3Csv2ParquetConversionError("partition_by parameter must be of type list")

        supported_modes = ['append', 'overwrite', 'error', 'ignore']
        if mode not in supported_modes:
            logging.error("mode {} is not formatted".format(mode))
            logging.error("mode must be one of type {}".format(",".join(supported_modes)))
            raise S3Csv2ParquetConversionError("mode must be one of type {}".
                                               format(",".join(supported_modes)))

        if not isinstance(separator, str):
            logging.error("seperator must be of type string got {} instead".format(str(type(separator))))
            raise S3Csv2ParquetConversionError("seperator must be of type string got {} instead".
                                               format(str(type(separator))))
