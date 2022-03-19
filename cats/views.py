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
    q = request.GET.get('search')
    error_msg = ''

    if not q:
        error_msg = 'Search something...'
        return render(request, 'cats/error_page.html', {'error_msg': error_msg})

    if CatProfile.objects.filter(slug__icontains=q):
        cat=CatProfile.objects.get(slug__icontains=q)
        return redirect(reverse('cats:show_cat', kwargs={'cat_name_slug':
                                                    cat.slug}))
    else:
        error_msg = 'No matched information founded...'
        return render(request, 'cats/error_page.html', {'error_msg': error_msg})

def show_cat(request, cat_name_slug):
    context_dic = {}
    a=request.user
    if request.user.is_authenticated:
        usr=request.user.userprofile.user_type
        context_dic['user_type']=usr
        
        delcom=request.POST.get('como',None)
        if delcom!=None and delcom!='':
            print('in delete')
            inx=CommentTable.objects.get(description=delcom)
            inx.delete()
        t=request.POST.get('tidiness',None)
        f=request.POST.get('fussinessc',None)
        fr=request.POST.get('friendliness',None)
        if t!=None and f!=None and fr!=None:
            rato=CatRatings()
            rato.uid=request.user.userprofile.uid
            rato.catname=CatProfile.objects.get(slug=cat_name_slug).breed
            rato.cid=CatProfile.objects.get(slug=cat_name_slug).cid
            rato.friendliness=fr
            rato.tidiness=t
            rato.fusiness=f
            rato.save()

    context_dic['slugo']=cat_name_slug
    try:
        cat = CatProfile.objects.get(slug=cat_name_slug)
        context_dic['cat'] = cat
        try:
            comment = CommentTable.objects.filter(cid=cat)
            context_dic['comment'] = comment
        except CommentTable.DoesNotExist:
            comment = None
            context_dic['comment'] = comment
    except CatProfile.DoesNotExist:
        cat = None
        context_dic['cat'] = cat
    add_comment(request, cat.slug)
    add_rating(request, cat.slug)
    return render(request, 'cats/cat_profile.html', context=context_dic)


def add_comment(request, cat_name_slug):
    if not request.user.is_authenticated:
        return redirect('users/login.html')
    if CommentTable.objects.count()>0:
        prevcom=CommentTable.objects.latest('postdate').description
    else:
        prevcom=None
    print(prevcom)
    coms=request.POST.get('comment',None)
    if coms!=None and coms!='' and coms!=prevcom:
        comso=CommentTable()
        catso=CatProfile.objects.get(slug=cat_name_slug)
        comso.uid=request.user.userprofile
        comso.description=coms
        comso.cid=catso
        comso.save()
    commento=CommentTable()
    commentform = CommentForm(instance=commento)
    if request.method == 'POST':
        commentform = CommentForm(request.POST,request.FILES,instance=commento)
        if commentform.is_valid():
            commentform.save()
            return redirect(reverse('cats:show_cat', kwargs={'cat_name_slug':
                                                cat_name_slug}))
    else:
        print(commentform.errors)
    return render(request, 'cats/cat_profile.html', {'commentform': commentform})

# use catrating models.
def add_rating(request, cat_name_slug):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('users/login.html'))
    ratingform = CatRatingsForm()
    if request.method == 'POST':
        ratingform = CatRatingsForm(request.POST)
        if ratingform.is_valid():
            ratingform.save(commit=True)
            return redirect(reverse('show_cat', kwargs={'cat_name_slug':
                                                cat_name_slug}))
    else:
        print(ratingform.errors)
    return render(request, 'cats/cat_profile.html', {'ratingform': ratingform})
