from django.shortcuts import render

from blog.models import Post

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def socialmedia(request):
    return render(request, "socialmedia.html")

def post_list(request):
    queryset = Post.objects.all()
    return render(request, "post_list.html", {"posts": queryset})
