
from django.urls import path

from . import views
from . import home_views
from . import profile_views
urlpatterns = [
    path("", home_views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/",profile_views.profile,name='profile')
]
