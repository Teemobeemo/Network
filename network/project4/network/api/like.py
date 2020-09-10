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

def dislike_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error':"You should be logged in to like a post"})
    post_id = request.GET.get('id')
    user = request.user
    try:
        post = Post.objects.get(id=post_id)

        likes_user_post = Like.objects.filter(user =user,post = post)
        if  not likes_user_post:
            return JsonResponse({"error":"You didnt like it before "})
        
        likes_user_post.delete()

        post.likes -=1
        post.save()

        response ={"likes":f"{post.likes}"}
        return JsonResponse(response)

    except Post.DoesNotExist:
        return JsonResponse({"error":"Post Does not Exist"})

# REname to if_liek_api
def get_like_api(request):
    # Check if user is logged in
    if not request.user.is_authenticated:
        return JsonResponse({'error':"You should be logged in to like a post"})

    # Get post id and user form the request body
    post_id = request.GET.get('id')
    user = request.user

    # Get the post. If not found return a error
    try:
        post = Post.objects.get(id=post_id)

        # Check if user liked the post and return appropriately
        like_by_user = Like.objects.filter(user=user,post =post)
        if like_by_user:
            return JsonResponse({"status":"True"})
        
        return JsonResponse({"status":"False"})

    except Post.DoesNotExist:
        return JsonResponse({"error":"Post Does not Exist"})