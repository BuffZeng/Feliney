from django import forms
from cats.models import CommentTable, CatProfile

class CatProfileForm(forms.ModelForm):

    class Meta:
        model = CatProfile
        fields = ('breed', 'price_range', 'friendliness','tidiness','fussiness','description')
        widgets={'description':forms.Textarea(attrs={'rows':6, 'cols':100}),}

class CommentForm(forms.ModelForm):
    description = forms.CharField(max_length=800,help_text="Please enter your comments.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = CommentTable
        fields = ('description', 'likes')
