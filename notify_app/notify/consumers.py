from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json


class NotificationConsumer(JsonWebsocketConsumer):

    group_name = 'notification'
    latest_recieved_message = None
    latest_id = None
    just_connected = False
    
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.just_connected = True
        self.accept()

    def notify(self, event):
        self.send_json(event['content'])

    def receive(self, text_data=None, bytes_data=None):
        self.latest_recieved_message = json.loads(text_data)

    def send_ping(self, event):
        self.latest_id = event['content']['id']
        self.send_json(event['content'])

    def check_pong(self, event):
        if self.just_connected == True:
            self.just_connected = False
            return

        if self.latest_recieved_message == None:
             self.close()
        else:
            if self.latest_recieved_message['id'] != self.latest_id or self.latest_recieved_message['message'] != 'pong':
                self.close()


   