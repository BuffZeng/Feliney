from django import forms
from cats.models import CommentTable, CatProfile

# class CatProfileForm(forms.ModelForm):
#     breed=forms.CharField(max_length=50,required=True)
#     price_range=forms.CharField(max_length=30)
#     friendliness=forms.FloatField(initial=3.0)
#     tidiness=forms.FloatField(initial=3.0)
#     fussiness=forms.FloatField(initial=3.0)
#     description = forms.CharField(max_length=800,initial="",required=False)
#     slug = forms.CharField(widget=forms.HiddenInput(), required=False)

#     class Meta:
#         model = CatProfile
#         fields = ('breed', 'price_range', 'friendliness', 'tidiness', 'fussiness', 'description')

class CommentForm(forms.ModelForm):
    description = forms.CharField(max_length=800,help_text="Please enter your comments.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = CommentTable
        fields = ('description', 'likes')

class RatingCatForm(forms.ModelForm):
    friendliness=forms.FloatField(widget=forms.HiddenInput(), initial=3.0)
    tidiness=forms.FloatField(widget=forms.HiddenInput(), initial=3.0)
    fussiness=forms.FloatField(widget=forms.HiddenInput(), initial=3.0)

    class Meta:
        model = CatProfile
        fields = ('friendliness', 'tidiness', 'fussiness')
