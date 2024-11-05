from django.db import models

# Create your models here.

class Post(models.Model):
  name = models.CharField(max_length=150)
  state = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  image = models.ImageField()
  desc = models.CharField(max_length=500)

def new_post(name, state, city, image, desc):
  post = Post.objects.create(name = name, state = state, city = city, image = image, desc = desc)
  return post

def all_posts():
  return Post.objects.all()