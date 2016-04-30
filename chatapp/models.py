from django.db import models
from datetime import datetime


class Message(models.Model):

    nick = models.CharField(max_length=20)
    #message_date = models.DateTimeField(default=datetime.now())
    message_date = models.DateTimeField(auto_now=True)
    message_content = models.CharField(max_length=80)

    def __str__(self):
        return str(self.message_date) + " " + str(self.nick)

    def print_message(self):
        return "[" + str(self.message_date).split(sep='.')[0] + "] " + str(self.nick) + ": " + self.message_content
