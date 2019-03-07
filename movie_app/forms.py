from django import forms
from .models import Movies
from django.contrib.auth.models import User

class AddMovie(forms.ModelForm):
    rating=forms.IntegerField()
    class Meta:
        model=Movies
        exclude=('admin',)

class REGFORM(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields = ('username', 'email','password')