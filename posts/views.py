from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post

# Create your views here.
def test_view(request):
    return HttpResponse("Hello, this is a test view!")

def home_view(request):
    return render(request, "base.html")

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", {"posts": posts})