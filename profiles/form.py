from django import forms
from django.forms import fields
from .models import Profile

class ProfileModelForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'avatar')