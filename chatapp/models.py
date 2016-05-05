from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    nick = models.ForeignKey(User)
    message_date = models.DateTimeField(auto_now=True)
    message_content = models.CharField(max_length=80)

    def __str__(self):
        return str(self.message_date) + " " + str(self.nick)

    def print_message(self):
        return "[" + str(self.message_date).split(sep='.')[0] + "] " + str(self.nick) + ": " + self.message_content

    @staticmethod
    def create_message(request):
        if request.method == "POST":
            if not request.user.is_anonymous():
                content = request.POST.get('msgbox', None)
                Message.objects.create(nick=request.user, message_content=content)
                return True
        return False

    @staticmethod
    def get_all():
        return Message.objects.order_by('message_date')

