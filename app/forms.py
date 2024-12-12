from django import forms


class StateFilter(forms.Form):
  state = forms.CharField(max_length=50)

class UrbexForm(forms.Form):
  name = forms.CharField(max_length=150)
  state = forms.CharField(max_length=50)
  city = forms.CharField(max_length=50)
  image = forms.ImageField()
  desc = forms.CharField(max_length=350, widget=forms.Textarea)
  lat = forms.CharField(max_length=60)
  long = forms.CharField(max_length=60)