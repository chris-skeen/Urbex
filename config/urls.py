from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("post", post_view, name="post"),
]
