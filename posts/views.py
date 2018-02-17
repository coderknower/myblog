from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login

from .models import Post
from .forms import PostForm


def post_create(request):
    form= PostForm()
    if request.method=='POST':
        print(request.POST)
    context={
        "form":form,
    }
    return render(request,"post_form.html",context)





def post_home(request):
    '''if request.user.is_autheticated():
        context={
            "title": "Home. You are logged in."
        }
        return render(request,"home.html",context)'''
    queryset= Post.objects.all()
    context = {
            "objectlist": queryset,
            "title": "You are not logged in"
        }
    return render(request,"login.html",context)
    #return HttpResponse("heyya ")


def post_detail(request, id=None):
    #instance=Post.objects.get(id=2)
    instance= get_object_or_404(Post, id=id)
    context = {
        "instance":instance,
        "title": instance.title,
    }
    return render(request,"post_detail.html",context)


def post_update(request):
    context = {
        "title": "Update"
    }
    return render(request,"home.html",context)


def post_delete(request):
    return HttpResponse("delete ")


