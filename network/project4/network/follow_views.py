from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from itertools import chain

from .models import Follow, Post


@login_required(login_url='/login')
def follow_view(request):
    # Get the current logged in user
    current_user = request.user

   # Get which page we are on (Pagination)
    page = request.GET.get("page", 1)

    # Get all the follow objects in which the user followed someone else
    follows = Follow.objects.filter(user_id=current_user)

    # List of posts id
    post_list_id = []

    # For each follow obj, loop
    for follow in follows:
        
        # Get posts by the followed user
        posts = Post.objects.filter(creator=follow.follow_id)

        for post in posts:
            post_list_id.append(post.id)

    post_list = Post.objects.filter(pk__in = post_list_id).order_by('-created_at')
    
    paginator = Paginator(post_list, 5)

    # Try to send the correct page using paginator
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "network/follow.html", {'posts': posts})
