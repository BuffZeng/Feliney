from django.shortcuts import redirect, render
from django.urls import reverse
from cats.forms import CommentForm, RatingCatForm
from .models import CatProfile, CommentTable
from django.http import HttpResponse

# Create your views here.
def search(request):
    q = request.GET.get('search')
    error_msg = ''

    if not q:
        error_msg = 'Search something...'
        return render(request, '', {'error_msg': error_msg})

    cat=CatProfile.objects.get(slug__icontains=q)
    return redirect(reverse('cats:show_cat', kwargs={'cat_name_slug':
                                                cat.slug}))


def show_cat(request, cat_name_slug):
    context_dic = {}

    try:
        cat = CatProfile.objects.get(slug=cat_name_slug)
        context_dic['cat'] = cat
        try:
            comment = CommentTable.objects.get(cid=cat.cid)
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
    # if not request.user.is_authenticated:
    #     return redirect(reverse('users/login'))
    commentform = CommentForm()
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            commentform.save(commit=True)
            return redirect(reverse('cats:show_cat', kwargs={'cat_name_slug':
                                                cat_name_slug}))
    else:
        print(commentform.errors)
    return render(request, 'cats/cat_profile.html', {'commentform': commentform})

def add_rating(request, cat_name_slug):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('users/login'))
    ratingform = RatingCatForm()
    if request.method == 'POST':
        ratingform = RatingCatForm(request.POST)
        if ratingform.is_valid():
            ratingform.save(commit=True)
            return redirect(reverse('show_cat', kwargs={'cat_name_slug':
                                                cat_name_slug}))
    else:
        print(ratingform.errors)
    return render(request, 'cats/cat_profile.html', {'ratingform': ratingform})
