from django.shortcuts import render

from .forms import NewPostForm
from .models import Post, UserProfile

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Home route (All posts route)
def index(request):
    new_post_form=None

    # Get which page we are on (Pagination)
    page = request.GET.get("page",1)
    
    # Check if user is logged in
    if request.user.is_authenticated:
        # Get the new post form if it is filled out.
        new_post_form = NewPostForm(request.POST or None)

        # Check if its valid
        if new_post_form.is_valid():

            # Create a new post obj with the data and add the creator
            post: Post = new_post_form.save(commit=False)
            post.creator = request.user
            post.save()

    # Get list of posts
    posts_list = Post.objects.all()

    posts_list = posts_list.order_by('-created_at')
    
    # Init paginator with the list and a limit
    # TODO change limit to 10
    paginator = Paginator(posts_list, 5)

    # Try to send the correct page using paginator
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Render the page with the form and the posts (with paginator)
    return render(request, "network/index.html",{"form":new_post_form,"posts":posts})