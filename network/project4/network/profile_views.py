from django.shortcuts import render

from .models import Post, UserProfile, Follow

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Profile page
def profile(request):
    # Get the username of the user (of whom the profile is going to be displayed)
    username = request.GET.get('id')

    # Get the page (paginator)
    page = request.GET.get("page", 1)

    # Init the variables to None
    user = None
    posts_of_user = None
    followers = None
    following = None

    isFollowing = False

    try:
        # Try to get the user based on the username provided
        user = UserProfile.objects.get(pk=username)

        # Get all the posts by the user
        posts_of_user_list = Post.objects.filter(creator=user)
        posts_of_user_list = posts_of_user_list.order_by('-created_at')

        # Get num of followers and following
        follows_follower = Follow.objects.filter(follow_id=user)
        followers = follows_follower.count()

        follow_following = Follow.objects.filter(user_id=user)
        following = follow_following.count()

        # Check if the requesting user follows or un follows the person
        for follow in follows_follower:
            if(follow.user_id.id == request.user.id):
                isFollowing = True
                break

        # init paginator
        paginator = Paginator(posts_of_user_list, 5)

        # Try to send the correct page using paginator
        try:
            posts_of_user = paginator.page(page)
        except PageNotAnInteger:
            posts_of_user = paginator.page(1)
        except EmptyPage:
            posts_of_user = paginator.page(paginator.num_pages)

    # Incase the user does not exist
    except UserProfile.DoesNotExist:
        print(f'Could not find user with username = {username}')

    """Render the page with the user,
                                posts,
                                followers,
                                following,
                                isFollowing variable"""

    return render(request, 'network/profile.html',
                  {"user1": user,
                   "posts": posts_of_user,
                   'followers': followers,
                   'following': following,
                   'isFollowing': isFollowing})
