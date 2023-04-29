from django.shortcuts import render
from .models import TodoItem

# Create your views here.

def all_posts(request):
    posts = TodoItem.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'todo/index.html', context)

def post_detail_views(request, id):
    post = TodoItem.objects.get(id=id)
    context = {
        'post': post,
        'id': id
    }
    return render(request, "todo/todo_detail.html", context)