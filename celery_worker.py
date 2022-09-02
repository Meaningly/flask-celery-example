from multiprocessing.pool import AsyncResult
import time
import os
from celery import Celery
from celery.utils.log import get_task_logger

redis_url = f"redis://{os.environ.get('REDIS_HOST','localhost')}:6379"
logger = get_task_logger(__name__)

app = Celery("tasks", broker=redis_url, backend=redis_url)

def load_task(task_id:str) -> AsyncResult:
    return app.AsyncResult(task_id)

@app.task
def sleep_message(seconds:int,message:str) -> str:
    logger.warn(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    logger.warn(f"Returning {message}")
    return message