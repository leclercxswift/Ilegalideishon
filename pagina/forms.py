from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class PdfUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['pdf_file']