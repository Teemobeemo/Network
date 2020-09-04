from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from network.models import UserProfile,Follow

@login_required(login_url='login')
def follow_api(request):
    nextA= request.GET.get('next')
    
    current_user = request.user

    to_follow = request.POST.get("to_follow")

    to_follow_user = UserProfile.objects.get(username=to_follow)

    following_user = Follow.objects.filter(user_id=current_user)
    for user in following_user:
        if (user.follow_id.username == to_follow):
            return redirect(nextA)

    follow = Follow(user_id=current_user,follow_id = to_follow_user)
    follow.save()

    return redirect(nextA)

def unfollow_api(request):
    nextA= request.GET.get('next')
    
    current_user = request.user

    to_follow = request.POST.get("to_follow")

    to_follow_user = UserProfile.objects.get(username=to_follow)

    following_user = Follow.objects.filter(user_id=current_user)

    for user in following_user:
        if (user.follow_id.username == to_follow):
            user.delete()
            return redirect(nextA)
    return redirect(nextA)


