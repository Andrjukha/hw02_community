# from typing import Any
from django.shortcuts import render, get_object_or_404

# from django.http import HttpResponse
from .models import Post, Group


# Главная страница
def index(request):

    posts = Post.objects.order_by("-pub_date")[:10]

    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    text = "Лев Толстой – зеркало русской революции."
    paragraph = "Группа тайных поклонников графа."

    context = {
        "group": group,
        "posts": posts,
        "text": text,
        "paragraph": paragraph,
    }
    return render(request, "posts/group_list.html", context)
