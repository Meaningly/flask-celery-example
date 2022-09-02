from flask import Flask, render_template,request
from celery.result import AsyncResult
import celery_worker

app = Flask(__name__)

@app.route("/")
def home():
    task_id = request.args.get("task_id")
    result:AsyncResult = None
    ready:bool = False
    message:str = None
    if task_id is not None:
        result = celery_worker.load_task(task_id)
    elif request.args.get("message") is not None:
        delay = int(request.args.get("delay"),10)
        success_message = request.args.get("message")
        result = celery_worker.sleep_message.delay(delay,success_message)
        task_id = result.task_id
    if result is not None:        
        ready = result.ready()
        if ready:
            message = result.get()

    return render_template("index.html",task_id=task_id,ready=ready,message=message)

