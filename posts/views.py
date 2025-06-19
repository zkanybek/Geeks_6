from django.shortcuts import render, HttpResponse
import random
from posts.models import Post

def test_view(request):
    return HttpResponse(f'hello, this is a test view, {random.randint(1, 100)}')

def homepage_view(request):
    return render(request, 'base.html')

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return HttpResponse("Post not found")
    
    return render(request, "posts/post_detail.html", context={"post": post})