from django.shortcuts import render,HttpResponse as Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
import os
from django.conf import settings

# all posts 
@api_view(['GET'])
def AllPosts(req):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

# add user
@api_view(['POST'])
def AddUser(req):

    if req.data.get('email'):
       
        user_data = {
            'email': req.data.get('email'),
            'name' :req.data.get('name'),
            'password':req.data.get('password')
        }

        # user = User(**user_data)
        if User.objects.filter(name=user_data['name']):
            err = {
            'msg' : "name already in use",
            }

            return Response(err)
        else:
            user = User(email = req.data.get('email'),name = req.data.get('name'), password= req.data.get('password'))
            user.save()  

        # Serialize the user instance
        serializer = UserSerializer(user)

        return Response(serializer.data)
    else:

        err = {
            'msg' : "Fill all the details",
        }

        return Response(err)
    
# add post
@api_view(['POST'])
def AddPost(req):

    if User.objects.filter(name=req.data.get('name')):
        author = User.objects.get(pk=req.data.get("name"))
        data = {
            "title" : req.data.get("title"),
            "content": req.data.get("content"),
            "author":author,
            "image":req.FILES.get("image"),
        }
        post = Post(**data)
        post.save()

        serializer = PostSerializer(post)
        return Response(serializer.data)
    else:
        return Response({
            "msg" :"Login to post a blog"
        })
    
# delete post
@api_view(["POST"])
def DeletePost(req):
    if User.objects.filter(name=req.data.get("name")):
        id = req.data.get("id")
        instance = Post.objects.get(author=req.data.get("name"),id=id)
        instance.delete()
        return Response({
            "msg" : True
        })
    else:
        return Response({
            "msg" : "Error occured can't delete"
        })
    
#update user
@api_view(["POST"])
def UpdateUser(req):

    if User.objects.filter(name=req.data.get("name")):

        name = req.data.get("name")
        email = req.data.get("email")
        password = req.data.get("password")

        user = User.objects.get(name=name)
        user.email = email
        user.password = password

        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:

        return Response({
            "msg" : "Cannot update user not found"
        })

# update post
@api_view(["POST"])
def UpdatePost(req):

    author = req.data.get("name")
    id = req.data.get("id")
    title = req.data.get("title")
    content = req.data.get("content")
    image = req.FILES.get("image")

    if User.objects.filter(name=author):

        if Post.objects.filter(id=id):

            post = Post.objects.get(id=id)

            post.title = title
            post.content = content
            post.image = image

            post.save()

            serialize = PostSerializer(post)
            return Response(serialize.data)
        else:

            return Response({
                "msg" : "Post not found"
            })
    else:

        return Response({
            "msg" : "login to update"
        })
