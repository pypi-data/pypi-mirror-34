import threading
from Queue import Queue, Empty
import time

RUNNING = 1
STOPPED = 0

class ThreadWorker(threading.Thread):

    def __init__(self, pool):
        super(ThreadWorker, self).__init__()
        self.pool = pool
        # subthreads terminates once the main thread end
        self.setDaemon(True)
        self.state = STOPPED

    def start(self):
        self.state = RUNNING
        super(ThreadWorker, self).start()

    def stop(self):
        self.state = STOPPED

    def run(self):
        while self.state is RUNNING:
            # don't use `Queue.empty` to check but use Exception `Empty`,
            # because another thread may put a job right after your checking
            try:
                job, args, kwargs = self.pool.jobs.get()
            except Empty:
                time.sleep(2)
                continue
            else:
                # do job
                try:
                    job(*args, **kwargs)
                    # self.pool.results.put(result)  # collect the result
                except Exception, e:
                    pass
                # finally:
                #     self.pool.jobs.task_done()


class ThreadPool(object):

    def __init__(self, size=1, queue_size=0):
        self.size = size
        self.jobs = Queue(maxsize=queue_size)
        self.threads = []

    def start(self):
        """start all threads"""
        for i in range(self.size):
            self.threads.append(ThreadWorker(self))

        for thread in self.threads:
            thread.start()

    def append_job(self, job, *args, **kwargs):
        self.jobs.put_nowait((job, args, kwargs))

    def join(self):
        """waiting all jobs done"""
        self.jobs.join()

    def queue_size(self):
        return self.jobs.qsize()

    def is_full(self):
        return self.jobs.qsize() >= self.jobs.maxsize