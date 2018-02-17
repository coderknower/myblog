from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import authenticate,login

from .views import post_home,post_create, post_detail,post_delete,post_update


urlpatterns = [
    url(r'^$', post_home),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),

]

