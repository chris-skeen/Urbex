from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("post", post_view, name="post"),
    path("about", about_view, name="about")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
