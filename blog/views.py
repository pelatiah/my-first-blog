from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, Comment
from django.utils import timezone


def index(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/index.html', {'posts': posts})

def oreva(request):
    return HttpResponse('<h2>This is the first try with the proper Configuration</h2>')

def post(request):
    return HttpResponse('<h2>Have you ever felt	that the world is more and more	about technology to	which you cannot (yet) relate? Have you	ever</h2>')
# Create your views here.
