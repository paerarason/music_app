from django.contrib.auth.models import User
from django import forms
from .models import Music
from django.contrib.auth.forms import UserCreationForm
class SignINForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']

class LoginINForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

class MUSICForm(forms.ModelForm):
    class Meta:
        model=Music
        fields=['name','description']