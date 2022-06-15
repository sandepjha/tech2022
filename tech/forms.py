from dataclasses import field
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from tech.models import Profile

class Signup(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class Login(AuthenticationForm):
    class Meta:
        model = Profile
        fields = "__all__"

class adduser(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"