
from django.urls import path

from . import views
from . import home_views
from . import profile_views
from . import follow_views
from .api import like
from .api import follow
from .api import edit
from .api import post_content
urlpatterns = [
    path("", home_views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/", profile_views.profile, name='profile'),
    path("following/", follow_views.follow_view, name='follow_views'),
    path("api/follow/",follow.follow_api,name='follow_api'),
    path("api/unfollow/",follow.unfollow_api,name='unfollow_api'),
    path("api/like/",like.like_api,name='like_api'),
    path("api/dislike/",like.dislike_api,name='dislike_api'),
    path("api/getlike/",like.get_like_api,name='get_like_api'),
    path('api/edit/',edit.edit_api,name='edit_api'),
    path('api/post/content',post_content.post_content_api,name='post_content_api'),

]
