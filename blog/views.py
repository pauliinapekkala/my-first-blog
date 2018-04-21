from django.shortcuts import render

from blog.models import Post

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html", {"title": "About"})

def socialmedia(request):
    return render(request, "socialmedia.html", {"title": "Social media"})

def post_list(request):
    queryset = Post.objects.all().order_by("-created_date")[:5]
    title = "Recent posts"
    return render(request, "post_list.html", {"posts": queryset, "title": title})
