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
    url(r'^del_message/', views.del_message, name='del_message'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^sent_mail/', views.sent_mail, name='sent_mail'),
    url(r'^$', views.chat, name='chat'),
    # url(r'^$', views.message, name='message'),

]

handler404 = 'views.custom_404'
