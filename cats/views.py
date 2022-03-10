from django.shortcuts import render
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.urls import reverse
from users.models import UserProfile, CatProfile, CommentTable
from django.http import HttpResponse

# Create your views here.
def cat_profile(request):
    current_cat=request.cid
    cat=CatProfile.objects.get(cat=current_cat)
    breed=cat.breed
    price_range=cat.price_range
    friendliness=cat.friendliness
    tidiness=cat.tidiness
    fussiness=cat.fussiness
    description=cat.description
    cat_info = {'breed':breed,'price_range':price_range,'friendliness':friendliness,'tidiness':tidiness,'fussiness':fussiness,'description':description}
    return render(request, 'cats/cat_profile.html', cat_info)

def add_comment(request):
    current_user=request.user
    user=UserProfile.objects.get(user=current_user)
    name=user.name
    current_cat=request.cid
    cat=CatProfile.objects.get(cat=current_cat)
    return render(request, 'cats/cat_profile.html')
    
