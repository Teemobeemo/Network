import json
from django.http import JsonResponse
from network.models import Post

def post_content_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error':"You should be logged in to like a post"})
    post_id = request.GET.get('id')

    try:
        post = Post.objects.get(id = post_id)
        return JsonResponse({'content':post.content})
    except Post.DoesNotExist:
        return JsonResponse(
            {'error':"Could not find the post you specukjaskjlj"})
