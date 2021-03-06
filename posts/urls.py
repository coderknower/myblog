from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.conf.urls.static import static

from .views import post_create, post_detail, post_delete, post_update, post_list


urlpatterns = [

    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),

]
