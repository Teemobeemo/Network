import json
from json.decoder import JSONDecodeError
from django.http import JsonResponse

from network.models import Post

def edit_api(request):
    current_user = request.user

    # Check if user is authenticated
    if not current_user.is_authenticated:
        return JsonResponse({'error':"You should be logged in to like a post"})
    
    rec_json =json.loads(request.body)
    # Get the post id
    post_id = rec_json['post']

    # Try to get the post and do stuff
    try:
        post = Post.objects.get(id = post_id)
        
        # Check if anyone else tries to edit the post
        if(post.creator != current_user):
            return JsonResponse({"error":"You can not edit other's posts"})
        
        # Get the content of the post
        post_content = rec_json['post_content']

        # Update the content and save
        post.content = post_content
        post.save()

        return JsonResponse({"status":"Edit successful"})

    except Post.DoesNotExist:
        return JsonResponse({"error":"Post does not exist"})