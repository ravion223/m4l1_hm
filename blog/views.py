from django.shortcuts import render
from blog.models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list": posts,
    }

    return render(
        request,
        template_name = "blog/post_list.html",
        context = context,
    )

def get_post_by_id(request, post_id):
    post = Post.objects.get(id = post_id)
    context = {
        "post": post
    }

    return render(
        request,
        template_name = "blog/post_content.html",
        context = context,
    )