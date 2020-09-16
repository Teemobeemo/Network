from django.http import JsonResponse

from network.models import UserProfile,Follow

def follow_api(request):
    current_user = request.user

    if not current_user.is_authenticated:
        return JsonResponse({'error':"You should be logged in to like a post"})

    to_follow = request.GET.get("to_follow")

    to_follow_user = UserProfile.objects.get(pk=to_follow)

    following_user = Follow.objects.filter(user_id=current_user)
    
    for user in following_user:
        if (user.follow_id.id == to_follow):
            return JsonResponse({'error':'Already following'})

    follow = Follow(user_id=current_user,follow_id = to_follow_user)
    follow.save()
    follows_follower = Follow.objects.filter(follow_id=to_follow_user)
    followers = follows_follower.count()
    return JsonResponse({"success":f'{followers}'})
 
def unfollow_api(request):
    current_user = request.user

    if not current_user.is_authenticated:
        return JsonResponse({'error':"You should be logged in to like a post"})

    to_follow = int(request.GET.get("to_follow"))

    to_follow_user = UserProfile.objects.get(pk=to_follow)
    try:
        following_user = Follow.objects.filter(user_id=current_user)

        for user in following_user:
            if (user.follow_id.id == to_follow):
                user.delete()
                follows_follower = Follow.objects.filter(follow_id=to_follow_user)
                followers = follows_follower.count()
                return JsonResponse({"success":f'{followers}'})
    except:
        return JsonResponse({"error":"You are not follwoing the user"})


