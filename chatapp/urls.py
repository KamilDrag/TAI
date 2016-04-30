from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^post/$', views.post, name='post'),
    url(r'^messages/$', views.messages, name='messages'),
    #url(r'^$', views.message, name='message'),

]
