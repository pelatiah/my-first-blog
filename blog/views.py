from django.shortcuts import render
from . models import Post, Comment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def index(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
# Create your views here.
