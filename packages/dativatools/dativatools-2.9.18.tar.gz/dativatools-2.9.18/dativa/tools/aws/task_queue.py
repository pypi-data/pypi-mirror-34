import queue
import time
import logging
logger = logging.getLogger("dativa.tools.aws.queue")


class Task():
    """
    An abstraction representing a Single task
    """

    def __init__(self, arguments):
        self.is_active = False
        self.arguments = arguments
        self.id = None
        self.retries = 0


class TaskQueue():
    """
    This is an abstract class that contains all required common functionality to
    support implementation of queues in aws client libraries.
    Two seperate queues are maintained:
    active_queue - Only tasks in this queue are allowed to run.
                   Once tasks are completed they are removed from this queue.
                   No of tasks in active queue <= max_size.
    pending_queue - Contains tasks that are awaiting execution.
                    Tasks from pending_queue are added to active_queue in FIFO
                    fashion.
    """
    
    def __init__(self, max_size, retry_limit=3):
        self.pending_tasks = queue.Queue()
        self.active_queue = []
        self.max_size = max_size
        self.retry_limit = retry_limit

    def add_task(self, arguments):
        '''This method adds a tasks to the pending_tasks queue'''
        task = Task(arguments)
        self.pending_tasks.put(task)
        self._empty_active_queue()
        self._fill_active_queue()
        return task

    def _empty_active_queue(self):
        """
        Removes completed task from active queue and populates freed spots with tasks
        in the front of pending_tasks queue
        """
        # Remove completed tasks from active queue
        for index, task in enumerate(self.active_queue):
            task = self._update_task_status(task)
            if not task.is_active:
                self.active_queue.pop(index)

    def _fill_active_queue(self):
        # Add add tasks to active queue if size of queue is less the max query limit
        for i in range(0, self.max_size - len(self.active_queue)):
            if not(self.pending_tasks.empty()):
                task = self.pending_tasks.get()
                self.active_queue.append(task)
                self._trigger_task(task)
            else:
                break

    def wait_for_completion(self):
        """
        This method runs until execution of all tasks is completed
        """
        while len(self.active_queue):
            logging.info("{} Tasks are awaiting exection".format(self.pending_tasks.qsize()))
            self._empty_active_queue()
            self._fill_active_queue()
            time.sleep(10)

    def _trigger_task(self, task):
        """
           This function should implement functionality to start aws task
           Once triggered is_active should be set to True
        """
        raise NotImplementedError("must be implemented by subclass")

    def _update_task_status(self, task):
        """Updates task status and returns updated task object
           Also handles retries
        """
        raise NotImplementedError("must be implemented by subclass")
