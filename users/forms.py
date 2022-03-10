from tkinter import Widget
from django.forms import ModelForm,Textarea
from django.contrib.auth.models import User
from django import forms

from .models import *

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('name', 'email_id', 'picture','breeds','about_me')
		widgets={'about_me':forms.Textarea(attrs={'rows':6, 'cols':100}),}

class CatPhotosForm(ModelForm):
	class Meta:
		model= CatPhotos
		fields =('picture','description')
		widgets={'description':forms.Textarea(attrs={'rows':6, 'cols':100}),}
