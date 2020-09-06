from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.test.client import JSON_CONTENT_TYPE_RE
from network.models import Like,Post

def like_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error':"You should be logged in to like a post"})
    post_id = request.GET.get('id')
    user = request.user
    try :
        post = Post.objects.get(id=post_id)

        likes_user_post = Like.objects.filter(user =user,post = post)
        if (likes_user_post):
            return JsonResponse({"error":"Already liked!"})

        like = Like()
        like.user = user
        like.post = post
        like.save()

        post.likes +=1
        post.save()
        response =  {"likes":f"{post.likes}"}
        return JsonResponse(response)
    except Post.DoesNotExist:
        return JsonResponse({"error":"Post Does not Exist"})

@login_required(login_url='login')
def dislike_api(request):
    return {"asd":"asdf"}

@login_required(login_url='login')
def get_like_api(request):
    return {"asd":"asdf"}

