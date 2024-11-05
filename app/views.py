from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import *

# Create your views here.

#  HOME VIEW AREA --------------------------------------------------------------------------------------------------------
def home_view(request):
  # Filter State Area.
  form = StateFilter(request.GET)

  # Display all data in sql.

  return render(request, "home.html", {"form":form})



#  POST VIEW AREA ----------------------------------------------------------------------------------------------------------
def post_view(request):
  form = FormPost(request.POST)

  return render(request, "post.html", {"form": form})

