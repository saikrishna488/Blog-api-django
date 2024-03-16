from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',AllPosts, name="home"),
    path('user', AddUser, name="adduser"),
    path('post', AddPost, name="addpost"),
    path('delete', DeletePost, name="deletepost"),
    path('updateuser', UpdateUser, name="updateuser"),
    path('updatepost', UpdatePost, name="updatepost")
]