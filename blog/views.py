from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, Comment


def index(request):
    return render(request, 'blog/index.html', {})

def oreva(request):
    return HttpResponse('<h2>This is the first try with the proper Configuration</h2>')

def post(request):
    return HttpResponse('<h2>Have you ever felt	that the world is more and more	about technology to	which you cannot (yet) relate? Have you	ever</h2>')
# Create your views here.
