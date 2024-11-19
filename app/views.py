from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .forms import *
from .models import *
from django.conf import settings
from django.conf.urls.static import static
from app.list_of_states import *
import datetime

# Create your views here.

#  HOME VIEW AREA --------------------------------------------------------------------------------------------------------
def home_view(request):
  form = StateFilter(request.GET)
  if form.is_valid():
      b4_state = form.cleaned_data['state']
      first_letter = b4_state[0].capitalize()
      rest_of_word = b4_state[1:]
      state = first_letter + rest_of_word
      if len(Post.objects.filter(state=state)) < 1:
        data = Post.objects.all()
        warning = 'We could not find this one :('
        sub = 'Please Try Again'
      else:
        data = Post.objects.filter(state=state)
        warning = ''
        sub = ''

      return render(request, "home.html", {"form":form, "data": data, "warn": warning, "sub": sub})
  
  return render(request, "home.html", {"form":form, "data": Post.objects.all()})
  



#  POST VIEW AREA ----------------------------------------------------------------------------------------------------------
def post_view(request):
  context = {}
  if request.method == "POST":
    form = UrbexForm(request.POST, request.FILES)
    if form.is_valid():
      print("hello!")
      name = form.cleaned_data.get('name')
      state = form.cleaned_data.get('state')
      for i in states:
        if state == i:
          state = form.cleaned_data.get('state')
          break
        else:
          state = 'Unknown'
          continue

      city = form.cleaned_data.get('city')
      image = form.cleaned_data.get('image')
      desc = form.cleaned_data.get('desc')
      lat = form.cleaned_data.get('lat')
      long = form.cleaned_data.get('long')
      print(lat)
      print(long)
      if lat != "" and long != "":
        print('here')
        f = open("MOCK_DATA-2.csv", "a")
        now = datetime.datetime.now()
        formatted_time = now.strftime("%I:%M:%S %p")

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        f.writelines(f"\n{city}, {state}, {formatted_date}, {formatted_time}, {long}, {lat}")


      obj = Post(name = name, 
                state = state,
                city = city,
                image= image,
                desc = desc,
                lat = lat,
                long = long,)
      obj.save()

  else:
    form = UrbexForm()
  context['form'] = form
  return render(request, "post.html", context)


def about_view(request):
  
  return render(request, "about.html", {})


def map_view(request):
  return render(request, "map.html", {})