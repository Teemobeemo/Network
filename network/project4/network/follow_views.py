from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Follow,UserProfile

@login_required(login_url='/login')
def follow_view(request):
    current_user = request.user
    follows = Follow.objects.filter(user_id=current_user)




    return render(request,"network/follow.html")