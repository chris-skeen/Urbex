from django.db import models

# Create your models here.

class Post(models.Model):
  name = models.CharField(max_length=150)
  state = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  image = models.ImageField(default="app/static/images/urbex-icon.png")
  desc = models.CharField(max_length=500)
  lat = models.CharField(max_length=60, blank=True, null=True)
  long = models.CharField(max_length=60, blank=True, null=True)

def new_post(name, state, city, image, desc, long, lat):
  post = Post.objects.create(name = name, state = state, city = city, image = image, desc = desc,lat = lat, long = long)
  return post

def all_posts():
  return Post.objects.all()