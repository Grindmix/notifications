from rest_framework import serializers
from notify.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'last_sent_at', 'title', 'type', 'content']