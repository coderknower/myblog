from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Post
from .forms import PostForm


def post_detail(request, id=None):

    instance= get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance":instance,

    }
    return render(request,"post_detail.html",context)


def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 25)  # Show 25 contacts per page
    #page = "shivam"
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
            "title": "List"
        }
    return render(request, "post_list.html", context)


def post_create(request):
    form= PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully Created")
        return (HttpResponseRedirect(instance.get_absolute_url()))

    context={
        "form":form,
    }
    return render(request,"post_form.html",context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    messages.success(request, "Successfully Deleted")
    instance.delete()
    return redirect("posts:list")

'''def post_home(request):
    if request.user.is_autheticated():
        context={
            "title": "Home. You are logged in."
        }
        return render(request,"home.html",context)
    queryset= Post.objects.all()
    context = {
            "object_list": queryset,
            "title": "You are not logged in"
        }
    return render(request, "index.html", context)'''
    #return HttpResponse("heyya ")

'''def post_update(request, id=None):
    instance= get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "<a href='#'>Succefully Saved</a>", extra_tags='html_safe')
        return(HttpResponseRedirect(instance.get_absolute_url()))
    else:
        messages.error(request,"Not Successfully Created")

    context = {
        "instance": instance,
        "title": instance.title,
        "form": form,
    }
    return render(request,"post_form.html",context)'''