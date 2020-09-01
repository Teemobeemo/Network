from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Follow,User

@login_required(login_url='/login')
def follow_view(request):
    return render(request,"network/follow.html")