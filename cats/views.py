from django.shortcuts import render

# Create your views here.
def cat_profile(request):
    return render(request, 'cats/cat_profile.html')
