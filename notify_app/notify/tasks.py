from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from notify.models import Notification
import uuid
import threading

@shared_task
def send_notification(data, time):

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('notification', {
                'type': 'notify',
                'content': data,
            })
    
    notification = Notification.objects.get(pk=data['id'])
    notification.last_sent_at = time
    notification.save()

@shared_task
def send_ping():

    id = str(uuid.uuid4())
    data = {'id': id, 'message': 'ping'}

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('notification', {
            'type': 'send_ping',
            'content': data,
    })

    t = threading.Timer(5, check_pong) # простите меня просто у меня не было других идей
    t.start()


def check_pong():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('notification', {
        'type': 'check_pong'
    })
