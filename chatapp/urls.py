from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^post/$', views.post, name='post'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^messages/$', views.messages, name='messages'),
    url(r'^activate/', views.activate, name='activate'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^$', views.chat, name='chat'),
    # url(r'^$', views.message, name='message'),

]
