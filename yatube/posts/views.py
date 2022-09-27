
from mimetypes import common_types
from multiprocessing import context
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group, User
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .utils import paginator_posts


# Главная страница
def index(request):
    template = "posts/index.html"
    posts = Post.objects.all()
    context = {
        "page_obj": paginator_posts(posts, request),
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()

    context = {
        "group": group,
        "page_obj": paginator_posts(posts, request),
    }
    return render(request, "posts/group_list.html", context)

def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        "author": user,
        "page_obj": paginator_posts(user.posts.select_related("group"), request),
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    page_obj = get_object_or_404(Post, id=post_id)
    count_posts = page_obj.author.posts.count()
    context = {
        "page_obj": page_obj,
        "count": count_posts,

    }
    return render(request, 'posts/post_detail.html', context) 

@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post=form.save(commit=False)
        post.author=request.user
        post.save()
        return redirect("posts:profile", username=post)
    context = {
        "form": form,
    }
    return render(request, "posts/create_post.html", context)

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if request.user != post.author:
        return redirect("posts:post_detail", post_id=pk)
    if form.is_valid():
        post.save()
        return redirect("posts:post_detail", post_id=pk)
    context = {"form": form, "is_edit": True}
    return render (request, 'posts/create_post.html', context)
