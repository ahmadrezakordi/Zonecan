from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class KelassorForm(forms.ModelForm):
    class Meta:
        model = Kelasor
        fields = '__all__'


class ParvandeForm(forms.ModelForm):
    class Meta:
        model = Parvande
        fields = ['title', 'name', 'description', 'date', 'file']
