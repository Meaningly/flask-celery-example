# Flask + Celery sample app

This is a simple Flask app that uses a Redis queue and results backend. It posts a
simple message to celery and polls for status.

This exists as a simple app that I can use to test some Terraform modules;
you should probably not use this application for anything.

# Running the app

To start the app and all of its pieces, run

```
docker-compose up
```

You can access the app via [http://localhost:5000/]

# Components

* Flask Web Server - `app.py`
* Celery Worker - `celery_worker.py`
* Redis Cache