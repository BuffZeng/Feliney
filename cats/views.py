from django.shortcuts import redirect, render, render_to_response
from django.urls import reverse
from cats.forms import CommentForm
from .models import CatProfile, CommentTable
from users.models import CatRatings
from users.forms import CatRatingsForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def search(request):
    # get the searched keyword
    q = request.GET.get('search')
    error_msg = ''

    if not q:
        # search in the wrong place
        error_msg = 'Search something...'
        return render(request, 'cats/error_page.html', {'error_msg': error_msg})

    if CatProfile.objects.filter(slug__icontains=q):
        # the keyword has been contained inside the slug name of cats
        cat=CatProfile.objects.get(slug__icontains=q)
        return redirect(reverse('cats:show_cat', kwargs={'cat_name_slug':
                                                    cat.slug}))
    else:
        # show error page when there is no matching
        error_msg = 'No matched information founded...'
        return render(request, 'cats/error_page.html', {'error_msg': error_msg})

def show_cat(request, cat_name_slug):
    # create context dic to store info
    context_dic = {}

    # authenrized user
    if request.user.is_authenticated:
        usr=request.user.userprofile.user_type
        context_dic['user_type']=usr
        
        # admin delete comment function
        delcom=request.POST.get('como',None)
        if delcom!=None and delcom!='':
            print('in delete')
            inx=CommentTable.objects.get(description=delcom)
            inx.delete()
        
        # get data from three attributes of the cat
        t=request.POST.get('tidiness',None)
        f=request.POST.get('fussinessc',None)
        fr=request.POST.get('friendliness',None)

        # must get three rating scores
        if t!=None and f!=None and fr!=None:
            rato=CatRatings()
            rato.uid=request.user.userprofile.uid
            rato.catname=CatProfile.objects.get(slug=cat_name_slug).breed
            rato.cid=CatProfile.objects.get(slug=cat_name_slug).cid
            rato.friendliness=fr
            rato.tidiness=t
            rato.fusiness=f
            # save the score inside the database
            rato.save()

    # get cat's slug name
    context_dic['slugo']=cat_name_slug

    try:
        cat = CatProfile.objects.get(slug=cat_name_slug)
        # get the cat profile object
        context_dic['cat'] = cat
        try:
            comment = CommentTable.objects.filter(cid=cat)
            # get all comment for this cat
            context_dic['comment'] = comment
        except CommentTable.DoesNotExist:
            comment = None
            context_dic['comment'] = comment
    except CatProfile.DoesNotExist:
        cat = None
        context_dic['cat'] = cat

    # two helping functions
    add_comment(request, cat.slug)
    add_rating(request, cat.slug)
    return render(request, 'cats/cat_profile.html', context=context_dic)


def add_comment(request, cat_name_slug):
    # check the user authenrization
    if not request.user.is_authenticated:
        return redirect('users/login.html')

    # check the history comment table
    if CommentTable.objects.count()>0:
        prevcom=CommentTable.objects.latest('postdate').description
    else:
        prevcom=None
    print(prevcom)

    # get the user's comment
    coms=request.POST.get('comment',None)
    if coms!=None and coms!='' and coms!=prevcom:
        comso=CommentTable()
        catso=CatProfile.objects.get(slug=cat_name_slug)
        comso.uid=request.user.userprofile
        comso.description=coms
        comso.cid=catso
        comso.save()
    commento=CommentTable()
    # call the commentform
    commentform = CommentForm(instance=commento)
    if request.method == 'POST':
        commentform = CommentForm(request.POST,request.FILES,instance=commento)
        if commentform.is_valid():
            # save comment to the database
            commentform.save()
            # refresh the page
            return redirect(reverse('cats:show_cat', kwargs={'cat_name_slug':
                                                cat_name_slug}))
    else:
        # print out the error message
        print(commentform.errors)
    return render(request, 'cats/cat_profile.html', {'commentform': commentform})

# use catrating models.
def add_rating(request, cat_name_slug):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('users/login.html'))

    # call the catratingfrom
    ratingform = CatRatingsForm()
    if request.method == 'POST':
        ratingform = CatRatingsForm(request.POST)
        if ratingform.is_valid():
            # save the data into the database
            ratingform.save(commit=True)
            # refresh the page
            return redirect(reverse('show_cat', kwargs={'cat_name_slug':
                                                cat_name_slug}))
    else:
        print(ratingform.errors)
    return render(request, 'cats/cat_profile.html', {'ratingform': ratingform})
