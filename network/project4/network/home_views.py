from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import NewPostForm
from .models import Post



def index(request):
    new_post_form=None
    if request.user.is_authenticated:
        new_post_form = NewPostForm(request.POST or None)

        if new_post_form.is_valid():
            print("form is valid")
            post: Post = new_post_form.save(commit=False)
            post.creator = request.user
            post.save()

    posts = Post.objects.all()


    return render(request, "network/index.html",{"form":new_post_form,"posts":posts})