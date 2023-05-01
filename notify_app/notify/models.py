from django.db import models

NOTIFICATION_TYPE = [
    ('SUCCESS', 'SUCCESS'),
    ('WARNING', 'WARNING'),
    ('FAIL', 'FAIL')
    ]


class Notification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_sent_at = models.DateTimeField(null=True)
    title = models.CharField(max_length=100, default='title')
    type = models.CharField(choices=NOTIFICATION_TYPE, default='SUCCESS', max_length=100)
    content = models.CharField(max_length=100, blank=True, default='content')