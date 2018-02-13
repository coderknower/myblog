from django.shortcuts import render
from django.http import HttpResponse


def post_home(request):
    return render(request,"home.html",{})
    #return HttpResponse("heyya ")


def post_detail(request):
    return HttpResponse("Detail ")


def post_list(request):
    return HttpResponse("Home")


def post_update(request):
    return HttpResponse("update")


def post_delete(request):
    return HttpResponse("delete ")

def post_create(request):
    return HttpResponse("create ")

