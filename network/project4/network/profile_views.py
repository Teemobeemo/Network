from django.shortcuts import render

from .models  import Post, UserProfile,Follow

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def profile(request):
    username = request.GET.get('username')

    page = request.GET.get("page",1)

    user = None
    posts_of_user = None
    followers = None
    following = None


    try:
        user = UserProfile.objects.get(username = username)
        posts_of_user_list = Post.objects.filter(creator = user)

        # Get num of followers and following
        follows_follower = Follow.objects.filter(follow_id=user)
        followers = follows_follower.count()
        
        follow_following = Follow.objects.filter(user_id=user)
        following = follow_following.count()

        paginator = Paginator(posts_of_user_list, 5)

        try:
            posts_of_user = paginator.page(page)
        except PageNotAnInteger:
            posts_of_user = paginator.page(1)
        except EmptyPage:
            posts_of_user = paginator.page(paginator.num_pages)

    except UserProfile.DoesNotExist:
        print(f'Could not find user with username = {username}')
    
    return render(request,'network/profile.html',
                        {"user1":user,
                        "posts":posts_of_user,
                        'followers':followers,
                        'following':following})
    
    
