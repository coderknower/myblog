from django.conf.urls import url
from django.contrib import admin

from .views import post_home,post_create, post_detail,post_delete,post_list,post_update


urlpatterns = [
    url(r'^home$', post_home),
    url(r'^create/$', post_create),
    url(r'^detail/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete$', post_delete),

]

