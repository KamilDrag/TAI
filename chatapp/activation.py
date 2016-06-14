from os import urandom
from base64 import b64encode
import smtplib


class Activation(object):

    @staticmethod
    def key_gen():
        key = b64encode(urandom(24)).decode('utf-8')
        key = ''.join(ch for ch in key if ch.isalnum())
        return key

    @staticmethod
    def activate_url(key):
        return "http://127.0.0.1:8000/activate/?id=" + key

    @staticmethod
    def send_mail(smtp, port, sender, login, password, receiver, key):
        server = smtplib.SMTP(smtp, port)
        server.login(login, password)
        msg = "\n Please visit " + Activation.activate_url(key) + " to end up registration."
        server.sendmail(sender, receiver, msg)
        server.close()