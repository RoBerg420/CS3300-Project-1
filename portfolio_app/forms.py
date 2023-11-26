from django.forms import ModelForm
from .models import Project, Portfolio

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UploadedFile


#create class for project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =('title', 'description')

#create class for portfolio form
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields =('title', 'about')

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].help_text = "Username cannot be longer than 50 characters. Letters, digits and @/./+/-/_ only."  
        self.fields['email'].help_text = "something@example.com"
  
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 50:
            raise ValidationError("Username cannot be longer than 50 characters.")
        return username
    

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='Username')

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']