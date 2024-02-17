from django.shortcuts import render
from blog.models import Author, Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list": posts
    }

    return render(
        request,
        template_name = "blog/post_list.html",
        context = context,
    )

def get_post_by_id(request, post_id):
    post = Post.objects.get(id = post_id)
    time_delta = post.published_recently()
    context = {
        "post": post,
        "time_delta": time_delta,
        "commentaries": post.commentaries.all()
    }

    return render(
        request,
        template_name = "blog/post_content.html",
        context = context,
    )

def author_posts(request, author_id):
    author = Author.objects.get(id = author_id) 
    context = {
        "author": author,
        "posts": author.posts.all()
    }

    return render(
        request,
        "blog/author_posts.html",
        context,
    )