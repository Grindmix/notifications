import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notify_app.settings')


app = Celery('notify_app')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "check_connection": {
        "task": "notify.tasks.send_ping",
        "schedule": 7.0
    }
}