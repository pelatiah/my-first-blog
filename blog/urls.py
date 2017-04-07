from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^oreva/', views.oreva, name='oreva'),
    url(r'^post/', views.post, name='post'),
]
