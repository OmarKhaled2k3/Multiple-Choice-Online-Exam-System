from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']

class UploadFileForm(forms.Form):
    file = forms.FileField()