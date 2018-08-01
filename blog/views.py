from django.shortcuts import render, get_object_or_404
from .models import Post

# def index(request):
#     context = {} 
#     return render(request, 'blog/index.html', context)
    
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts}) 

def notes(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/home.html', {'post': post})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})