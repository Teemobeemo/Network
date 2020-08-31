from django.shortcuts import render

from .models  import Post, User

def profile(request):
    username = request.GET.get('username')

    user = None
    posts_of_user = None
    try:
        user = User.objects.get(username = username)
        posts_of_user = Post.objects.filter(creator = user)

    except User.DoesNotExist:
        print(f'Could not find user with username = {username}')
    
    return render(request,'network/profile.html',{"user1":user,"posts":posts_of_user})
    
    
