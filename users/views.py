from multiprocessing.dummy import current_process
from django.shortcuts import render
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.urls import reverse
from django.forms import inlineformset_factory
from users.forms import CatPhotosForm
from users.models import CatPhotos

from users.models import UserProfile
from django.http import HttpResponse
from users.forms import UserProfileForm
# Create your views here.
def index(request):
    current_user=request.user
    print(current_user)
    user=UserProfile.objects.get(user=current_user)
    name=user.name
    user_type=user.user_type
    email=user.email_id
    since=user.member_since
    breeds=user.breeds
    about_me=user.about_me
    picture=user.picture.url
    cat1,cat2,cat3,cat4=CatPhotos.objects.filter(uid=user.uid).order_by('-uploaddate')[:4]
    print(cat2.picture.url)
    response = render(request, 'users/indexo.html',{'name':name,'user_type':user_type,'email_id':email,'since':since,'breeds':breeds,'about_me':about_me,'picture':picture,'cat1':cat1,'cat2':cat2,'cat3':cat3,'cat4':cat4})
    return response

def personal_info(request):
    return render(request, 'users/index.html')

def all_coments(request):
    response = render(request, 'users/all_comments.html')
    return response

def edit_ratings(request):
    response = render(request, 'users/edit_ratings.html')
    return response

def upload_image(request):
    current_user_id=request.user.userprofile.uid
    cato=CatPhotos(uid=current_user_id)
    gh=CatPhotosForm(instance=cato)
    if request.method=='POST':
        gh=CatPhotosForm(request.POST,request.FILES,instance=cato)
        if gh.is_valid():
            gh.save()
    context={'form':gh}
    response = render(request, 'users/upload_photos.html',context)
    return response

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('users:home_page'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'users/login.html')

def home_page(request):
    user=request.user
    print(user)
    return render(request,'users/index.html')

def edit_user(request):
    current_user=request.user
    usero=UserProfile.objects.get(user=current_user)
    gh=UserProfileForm(instance=usero)
    if request.method=='POST':
        gh=UserProfileForm(request.POST,request.FILES,instance=usero)
        if gh.is_valid():
            gh.save()
    context={'form':gh}
    return render(request, 'users/edit_info.html', context)
	

def user_logout(request):
    logout(request)
    return redirect(reverse('users:home_page'))

def add_cat(request):
    return render(request,'users/add_cat.html')