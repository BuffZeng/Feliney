from tkinter import Widget
from django.forms import HiddenInput, ModelForm,Textarea
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
		widgets={'description':forms.Textarea(attrs={'rows':4, 'cols':30}),}


class CatRatingsForm(ModelForm):
	class Meta:
		model= CatRatings
		fields = ('catname','fusiness','friendliness','tidiness')	

class CatimessageForm(ModelForm):
	class Meta:
		model= Catimessage
		fields =('messagebody',)
		widgets={'messagebody':forms.Textarea(attrs={'rows':6, 'cols':100}),}

class DraftmessageForm(ModelForm):
	class Meta:
		model= Catimessage
		fields =('messagereceive','messagebody')
		widgets={'messagebody':forms.Textarea(attrs={'rows':6, 'cols':100}),}


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','password')

class UserRegProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('email_id','picture','user_type','breeds','about_me')
		widgets={'about_me':forms.Textarea(attrs={'rows':6, 'cols':100}),}
