"""
定时任务
"""
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler.configure(executors=executors, job_defaults=job_defaults)
scheduler.start()


def init_task():
    """

    :return:
    """
