from pyexpat import model
from django import forms
from cats.models import CommentTable, CatProfile
from users.models import UserProfile

class CatProfile(forms.Model):
    breed=forms.CharField(max_length=50,required=True)
    price_range=forms.CharField(max_length=30)
    friendliness=forms.FloatField(initial=3.0)
    tidiness=forms.FloatField(initial=3.0)
    fussiness=forms.FloatField(initial=3.0)
    description = forms.CharField(max_length=800,initial="",required=False)

    class Meta:
        model = CatProfile

class CommentForm(forms.ModelForm):
    description = forms.CharField(max_length=800,help_text="Please enter your comments.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = CommentTable