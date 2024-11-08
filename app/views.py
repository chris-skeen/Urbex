from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .forms import *
from .models import *
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.

#  HOME VIEW AREA --------------------------------------------------------------------------------------------------------
def home_view(request):
  form = StateFilter(request.GET)
  context = {}
  context['data'] = Post.objects.all()
  print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
  return render(request, "home.html", context)
  



#  POST VIEW AREA ----------------------------------------------------------------------------------------------------------
def post_view(request):
  context = {}
  if request.method == "POST":
    form = UrbexForm(request.POST, request.FILES)
    if form.is_valid():
      print("hello!")
      name = form.cleaned_data.get('name')
      state = form.cleaned_data.get('state')
      city = form.cleaned_data.get('city')
      image = form.cleaned_data.get('image')
      desc = form.cleaned_data.get('desc')
      obj = Post(name = name, 
                state = state,
                city = city,
                image= image,
                desc = desc)
      obj.save()

  else:
    form = UrbexForm()
  context['form'] = form
  return render(request, "post.html", context)

