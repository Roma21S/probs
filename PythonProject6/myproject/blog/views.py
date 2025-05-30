from django.shortcuts import render
from .models import Post

# Отображение списка всех записей
def post_list(request):
    posts = Post.objects.all().order_by('-published_at')  # выбираем все записи по дате
    return render(request, 'blog/post_list.html', {'posts': posts})