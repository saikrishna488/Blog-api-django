from django.db import models
import os
from django.conf import settings
from django.core.files.storage import default_storage

class User(models.Model):
    email = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50, primary_key=True)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
def userImagePath(instance,imgName):

    filepath = f'images/{instance.author}/{imgName}'
    return filepath



class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=userImagePath,verbose_name='Blog Picture',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title