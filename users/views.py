from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.urls import reverse
from users.forms import DraftmessageForm, CatimessageForm, CatRatingsForm, CatPhotosForm, UserProfileForm, UserRegProfileForm, UserForm
from users.models import Catimessage, CatRatings, CatPhotos, UserProfile
from cats.models import CatProfile, CommentTable
from cats.forms import CatProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.

# user profile page
def index(request):
    a=request.user
    # authorized user
    if a!='AnonymousUser':
        # get the cat name
        catorama=request.POST.get('catname',None)
        if catorama!=None:
            # get cats info
            tidiness=request.POST.get('tidiness',None)
            fusiness=request.POST.get('fusiness',None)
            friendliness=request.POST.get('friendliness',None)
            catobecjto=CatRatings.objects.get(uid=request.user.userprofile.uid,catname=catorama)
            catobecjto.tidiness=tidiness
            catobecjto.friendliness=friendliness
            catobecjto.fusiness=fusiness
            # save the cat data into database
            catobecjto.save()

        # get the current user
        current_user=request.user
        print(current_user)

        # get user info
        user=UserProfile.objects.get(user=current_user)
        name=user.name
        user_type=user.user_type
        email=user.email_id
        since=user.member_since
        breeds=user.breeds
        about_me=user.about_me
        picture=user.picture.url

        # show the gallary only if cats images greater than 4
        if CatPhotos.objects.filter(uid=user.uid).count()>=4:
            cat1,cat2,cat3,cat4=CatPhotos.objects.filter(uid=user.uid).order_by('-uploaddate')[:4]
        else:
            # show empy gallary
            cat1=None
            cat2=None
            cat3=None
            cat4=None
        # save all user info into response
        response = render(request, 'users/indexo.html',{'name':name,'user_type':user_type,'email_id':email,'since':since,'breeds':breeds,'about_me':about_me,'picture':picture,'cat1':cat1,'cat2':cat2,'cat3':cat3,'cat4':cat4})
        return response
    else:
        return render(request,'users/indexo.html')

# show personal info
def personal_info(request):
    return render(request, 'users/index.html')

# show all comments in the personal files
def all_coments(request):
    # get comment that user want to delete
    delcom=request.POST.get('como',None)
    if delcom!=None and delcom!='':
        print('in delete')
        # match the comment to the database
        inx=CommentTable.objects.get(description=delcom,uid=request.user.userprofile.uid)
        if inx!=None:
            inx.delete()
    # get current user's uid
    current_user=request.user.userprofile.uid
    # get all comemnt of current user
    all_comments=CommentTable.objects.filter(uid=current_user)
    # return all the comments
    tups=[(a.description,a.cid.breed) for a in all_comments]
    context={'tups':tups}
    response = render(request, 'users/all_comments.html',context)
    return response

# user edit rating
def edit_ratings(request):
    # get the object of cat
    catothree=request.POST.get('cat',None)
    print(catothree)
    # get current user
    current_user=request.user.userprofile.uid
    # get all rating history
    all_ratings=CatRatings.objects.get(uid=current_user,catname=catothree)
    # call catratingform
    newform=CatRatingsForm(instance=all_ratings)
    if request.method=='POST':
        newform=CatRatingsForm(instance=all_ratings)
        if newform.is_valid():
            # save data into the database
            newform.save()
            return redirect(reverse('users:index'))
    # save form and passed to front end
    context={'form':newform,'msg':'saved'}
    return render(request, 'users/edit_ratings.html',context)

# get all past rating history for a user
def pre_cat_ratings(request):
    # get all rating from the current user
    allcatos=CatRatings.objects.filter(uid=request.user.userprofile.uid)
    breeds=[x.catname for x in allcatos]
    print(breeds)
    return render(request, "users/pre_cat_ratings.html",{"allcats":breeds})

# function to upload images
def upload_image(request):
    # get the current user
    current_user=request.user
    # get the uid
    user_id=UserProfile.objects.get(user=current_user).uid
    # get the cat image by upload by user
    catio=CatPhotos.objects.filter(uid=user_id)
    # get the list of images
    a=[x.picture.url for x in catio]
    current_user_id=request.user.userprofile.uid
    cato=CatPhotos(uid=current_user_id)
    gh=CatPhotosForm(instance=cato)
    if request.method=='POST':
        # submit by call catphotosform
        gh=CatPhotosForm(request.POST,request.FILES,instance=cato)
        if gh.is_valid():
            # save data to the database
            gh.save()
            return redirect(reverse('users:upload_image'))
    # send forms to the front end
    context={'form':gh,'cato':a}
    response = render(request, 'users/upload_photos.html',context)
    return response
    
def login(request):
    if request.method == 'POST':
        # get user input for username and password
        username = request.POST.get('username')
        password = request.POST.get('password')
        # autherized the user
        user = authenticate(username=username, password=password)
        if user:
            # check the user is active or not
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('users:home_page'))
            else:
                return HttpResponse("Your Feliney account is disabled.")
        else:
            # error message if the input of users are invalid
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'users/login.html')

# the main home page
def home_page(request):
    # get the current user
    user=request.user
    # check the the first cat
    maxc=CatProfile.objects.all().order_by("-cid")[0].cid
    for x in range(1,maxc+1):
        # get all users rating
        votes=CatRatings.objects.filter(cid=x).count()
        if votes==0:
            # if no rating, all score remain in default as 3.0
            catins=CatProfile.objects.get(cid=x)
            catins.friendliness=3.0
            catins.tidiness=3.0
            catins.fussiness=3.0
            catins.save()
        else:
            # calculate the score of each attribute.
            catfriend= (CatRatings.objects.filter(cid=x).aggregate(Sum('friendliness'))['friendliness__sum'])/votes
            cattidy= (CatRatings.objects.filter(cid=x).aggregate(Sum('tidiness'))['tidiness__sum'])/votes
            catfusy= (CatRatings.objects.filter(cid=x).aggregate(Sum('fusiness'))['fusiness__sum'])/votes
            catres= CatProfile.objects.get(cid=x)
            catres.friendliness=catfriend
            catres.tidiness=cattidy
            catres.fussiness=catfusy
            # save all data into the database
            catres.save()
    context_dic = {}
    # get four type of ranking: general, friendliness, fussiness, tidiness
    context_dic['general'] = CatProfile.objects.order_by('-friendliness', '-fussiness', '-tidiness')[:8]
    context_dic['friendliness'] = CatProfile.objects.order_by('-friendliness')[:8]
    context_dic['fussiness'] = CatProfile.objects.order_by('-fussiness')[:8]
    context_dic['tidiness'] = CatProfile.objects.order_by('-tidiness')[:8]
    print(user)
    return render(request,'users/index.html', context=context_dic)
    
# edit user profile
def edit_user(request):
    # get current user
    current_user=request.user
    # get current user object
    usero=UserProfile.objects.get(user=current_user)
    gh=UserProfileForm(instance=usero)
    if request.method=='POST':
        gh=UserProfileForm(request.POST,request.FILES,instance=usero)
        if gh.is_valid():
            # save modified data into database
            gh.save()
            return redirect(reverse('users:index'))
    # save forms and send to the front end
    context={'form':gh,'msg':'saved'}
    return render(request, 'users/edit_info.html',context)

# register a user
def register(request):
    # a flag set to false
    registered = False
    # get username and uploaded picture
    username = request.POST.get('username','')
    picture = request.POST.get('picture','')
    if request.method == 'POST':
        print(1)
        # call userform and userregprofileform
        user_form = UserForm(request.POST)
        profile_form = UserRegProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # save data into database
            user = user_form.save()

            # get user password, username and save to database
            user.set_password(user.password)
            user.name=username
            user.save()

            # get form saved into the database
            profile = profile_form.save(commit=False)
            profile.user = user 
            rt=username.replace('_',' ')
            profile.name = rt
            # upload the pictures
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

# logout function
def user_logout(request):
    logout(request)
    # after logout, redirect into home page
    return redirect(reverse('users:home_page'))

# admin add cat
def add_cat(request):
    cato=CatProfile()
    # call catprofile form
    gh=CatProfileForm(instance=cato)
    if request.method=='POST':
        gh=CatProfileForm(request.POST,request.FILES,instance=cato)
        if gh.is_valid():
            # save cat info to database
            gh.save()
            return redirect(reverse('users:index'))
    context={'form':gh,'msg':'saved'}
    return render(request,'users/add_cat.html',context)

# users replying messages
def messaging(request):
    body=request.POST.get('messagebody',None)
    rec=request.POST.get('rec',None)
    # get message info
    if body!=None:
        cmes=Catimessage()
        cmes.catmessager=request.user
        cmes.messagesend=request.user
        cmes.messagereceive=User.objects.get(username=rec)
        cmes.messagebody=body
        cmes.save()
    
    # get the current user
    current_user=request.user
    # get all messages
    all_messages=Catimessage.objects.filter(messagereceive=current_user).order_by('-messagesend')
    tups=[(a.messagesend,a.messagebody,a.sentdate) for a in all_messages]
    context={'tups':tups}
    response = render(request, 'users/messaging.html',context)
    return response

# users sending messages
def new_message(request):
    sendo=request.POST.get('sender',None)
    # get possible usernamen to send
    usero=User.objects.get(username=sendo)
    cato=Catimessage(catmessager=request.user,messagesend=request.user,messagereceive=usero)
    # call catimessageform
    gh=CatimessageForm(instance=cato)
    if request.method=='POST':
        gh=CatimessageForm(instance=cato)
        print(gh)
        if gh.is_valid():
            # save message into database
            gh.save()
            return redirect(reverse('users:upload_image'))
    # get sender username
    namo=UserProfile.objects.get(user=usero).name
    context={'form':gh,'name':namo,'recieve':usero}
    response = render(request, 'users/new_message.html',context)
    return response

# choose user to send messages
def draftnew(request):
    drafto=Catimessage(catmessager=request.user,messagesend=request.user)
    # call draftmessageform
    gh=DraftmessageForm(instance=drafto)
    if request.method=='POST':
        gh=DraftmessageForm(request.POST,request.FILES,instance=drafto)
        if gh.is_valid():
            # save message into database
            gh.save()
            return redirect(reverse('users:messaging'))
    context={'form':gh,'msg':'saved'}
    return render(request,'users/draft_new.html',context)

