from django import forms
from .models import Message
import django.contrib.auth as auth
from django.contrib.auth.models import User
#nowe
from django import forms
from .models import SignUp
from re import match


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message_content']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(u'User: %s not exist!' % username)
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if not (user and user.is_active):
            raise forms.ValidationError(u'Incorrect password!')
        return password


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['password'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control'
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(u'User: %s exist!' % username)
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 5:
            raise forms.ValidationError(u'Password is too short!')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise forms.ValidationError(u'Please enter correct e-mail!')
        return email

