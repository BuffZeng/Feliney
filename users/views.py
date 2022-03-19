from multiprocessing.dummy import current_process
from django.shortcuts import render
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.urls import reverse
from django.forms import inlineformset_factory
from users.forms import DraftmessageForm
from users.forms import CatimessageForm
from users.models import Catimessage
from users.forms import CatRatingsForm
from users.models import CatRatings
from cats.models import CatProfile
from users.forms import CatPhotosForm
from cats.forms import CatProfileForm
from cats.models import CommentTable
from users.models import CatPhotos
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import UserProfile
from django.http import HttpResponse
from users.forms import UserProfileForm,UserRegProfileForm,UserForm
from cats.forms import CatProfile
from django.db.models import Sum
# Create your views here.
def index(request):
    a=request.user
    if a!='AnonymousUser':
        catorama=request.POST.get('catname',None)
        if catorama!=None:
            tidiness=request.POST.get('tidiness',None)
            fusiness=request.POST.get('fusiness',None)
            friendliness=request.POST.get('friendliness',None)
            catobecjto=CatRatings.objects.get(uid=request.user.userprofile.uid,catname=catorama)
            catobecjto.tidiness=tidiness
            catobecjto.friendliness=friendliness
            catobecjto.fusiness=fusiness
            catobecjto.save()
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
        if CatPhotos.objects.filter(uid=user.uid).count()>=4:
            cat1,cat2,cat3,cat4=CatPhotos.objects.filter(uid=user.uid).order_by('-uploaddate')[:4]
        else:
            cat1=None
            cat2=None
            cat3=None
            cat4=None
        response = render(request, 'users/indexo.html',{'name':name,'user_type':user_type,'email_id':email,'since':since,'breeds':breeds,'about_me':about_me,'picture':picture,'cat1':cat1,'cat2':cat2,'cat3':cat3,'cat4':cat4})
        return response
    else:
        return render(request,'users/indexo.html')

def personal_info(request):
    return render(request, 'users/index.html')

def all_coments(request):
    current_user=request.user.userprofile.uid
    all_comments=CommentTable.objects.filter(uid=current_user)
    tups=[(a.description,a.cid.breed) for a in all_comments]
    context={'tups':tups}
    response = render(request, 'users/all_comments.html',context)
    return response

def edit_ratings(request):
    catothree=request.POST.get('cat',None)
    print(catothree)
    current_user=request.user.userprofile.uid
    all_ratings=CatRatings.objects.get(uid=current_user,catname=catothree)
    newform=CatRatingsForm(instance=all_ratings)
    if request.method=='POST':
        newform=CatRatingsForm(instance=all_ratings)
        if newform.is_valid():
            newform.save()
            return redirect(reverse('users:index'))
    context={'form':newform,'msg':'saved'}
    return render(request, 'users/edit_ratings.html',context)

def pre_cat_ratings(request):
    allcatos=CatRatings.objects.filter(uid=request.user.userprofile.uid)
    breeds=[x.catname for x in allcatos]
    print(breeds)
    return render(request, "users/pre_cat_ratings.html",{"allcats":breeds})


def upload_image(request):
    current_user=request.user
    user_id=UserProfile.objects.get(user=current_user).uid
    catio=CatPhotos.objects.filter(uid=user_id)
    a=[x.picture.url for x in catio]
    current_user_id=request.user.userprofile.uid
    cato=CatPhotos(uid=current_user_id)
    gh=CatPhotosForm(instance=cato)
    if request.method=='POST':
        gh=CatPhotosForm(request.POST,request.FILES,instance=cato)
        if gh.is_valid():
            gh.save()
            return redirect(reverse('users:upload_image'))
    context={'form':gh,'cato':a}
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
    maxc=CatProfile.objects.all().order_by("-cid")[0].cid
    for x in range(1,maxc+1):
        votes=CatRatings.objects.filter(cid=x).count()
        if votes==0:
            catins=CatProfile.objects.get(cid=x)
            catins.friendliness=3.0
            catins.tidiness=3.0
            catins.fussiness=3.0
            catins.save()
        else:
            catfriend= (CatRatings.objects.filter(cid=x).aggregate(Sum('friendliness'))['friendliness__sum'])/votes
            cattidy= (CatRatings.objects.filter(cid=x).aggregate(Sum('tidiness'))['tidiness__sum'])/votes
            catfusy= (CatRatings.objects.filter(cid=x).aggregate(Sum('fusiness'))['fusiness__sum'])/votes
            catres= CatProfile.objects.get(cid=x)
            catres.friendliness=catfriend
            catres.tidiness=cattidy
            catres.fussiness=catfusy
            catres.save()
    context_dic = {}
    context_dic['general'] = CatProfile.objects.order_by('-friendliness', '-fussiness', '-tidiness')[:8]
    context_dic['friendliness'] = CatProfile.objects.order_by('-friendliness')[:8]
    context_dic['fussiness'] = CatProfile.objects.order_by('-fussiness')[:8]
    context_dic['tidiness'] = CatProfile.objects.order_by('-tidiness')[:8]
    print(user)
    return render(request,'users/index.html', context=context_dic)
    
def edit_user(request):
    current_user=request.user
    usero=UserProfile.objects.get(user=current_user)
    gh=UserProfileForm(instance=usero)
    if request.method=='POST':
        gh=UserProfileForm(request.POST,request.FILES,instance=usero)
        if gh.is_valid():
            gh.save()
            return redirect(reverse('users:index'))
    context={'form':gh,'msg':'saved'}
    return render(request, 'users/edit_info.html',context)

def register(request):
    registered = False
    username = request.POST.get('username','')
    picture = request.POST.get('picture','')
    if request.method == 'POST':
        print(1)
        user_form = UserForm(request.POST)
        profile_form = UserRegProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.name=username
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user 
            rt=username.replace('_',' ')
            profile.name = rt
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
            registered = True
        else:
              print(user_form.errors, profile_form.errors)
    else:
            print(2)
            user_form = UserForm()
            profile_form = UserRegProfileForm()
    return render(request, 'users/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

	

def user_logout(request):
    logout(request)
    return redirect(reverse('users:home_page'))

def add_cat(request):
    cato=CatProfile()
    gh=CatProfileForm(instance=cato)
    if request.method=='POST':
        gh=CatProfileForm(request.POST,request.FILES,instance=cato)
        if gh.is_valid():
            gh.save()
            return redirect(reverse('users:index'))
    context={'form':gh,'msg':'saved'}
    return render(request,'users/add_cat.html',context)

def messaging(request):
    body=request.POST.get('messagebody',None)
    rec=request.POST.get('rec',None)
    if body!=None:
        cmes=Catimessage()
        cmes.catmessager=request.user
        cmes.messagesend=request.user
        cmes.messagereceive=User.objects.get(username=rec)
        cmes.messagebody=body
        cmes.save()
    current_user=request.user
    all_messages=Catimessage.objects.filter(messagereceive=current_user).order_by('-messagesend')
    tups=[(a.messagesend,a.messagebody,a.sentdate) for a in all_messages]
    context={'tups':tups}
    response = render(request, 'users/messaging.html',context)
    return response

def new_message(request):
    sendo=request.POST.get('sender',None)
    usero=User.objects.get(username=sendo)
    cato=Catimessage(catmessager=request.user,messagesend=request.user,messagereceive=usero)
    gh=CatimessageForm(instance=cato)
    if request.method=='POST':
        gh=CatimessageForm(instance=cato)
        print(gh)
        if gh.is_valid():
            gh.save()
            return redirect(reverse('users:upload_image'))
    namo=UserProfile.objects.get(user=usero).name
    context={'form':gh,'name':namo,'recieve':usero}
    response = render(request, 'users/new_message.html',context)
    return response

def draftnew(request):
    drafto=Catimessage(catmessager=request.user,messagesend=request.user)
    gh=DraftmessageForm(instance=drafto)
    if request.method=='POST':
        gh=DraftmessageForm(request.POST,request.FILES,instance=drafto)
        if gh.is_valid():
            gh.save()
            return redirect(reverse('users:messaging'))
    context={'form':gh,'msg':'saved'}
    return render(request,'users/draft_new.html',context)

