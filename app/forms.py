from django import forms


class StateFilter(forms.Form):
  state = forms.CharField(max_length=50, required=False)

class FormPost(forms.Form):
  name = forms.CharField(max_length=150)
  state = forms.CharField(max_length=50)
  city = forms.CharField(max_length=50)
  image = forms.ImageField()
  desc = forms.CharField(max_length=500)