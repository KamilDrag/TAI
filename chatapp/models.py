from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    nick = models.ForeignKey(User)
    message_date = models.DateTimeField(auto_now=True)
    message_content = models.CharField(max_length=80)
    models.ImageField()

    def __str__(self):
        return str(self.message_date) + " " + str(self.nick)

    def print_message(self):
        return self.message_content

    def print_info(self):
        return str(self.message_date).split(sep='.')[0] + " | " + str(self.nick)

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

    def is_staff(self):
        return User.objects.get_by_natural_key(self.nick)


# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=120, blank=True, null=True)
    password = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    key = models.CharField(max_length=120)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.email
