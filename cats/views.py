from django.shortcuts import redirect, render
from cats.forms import CommentForm
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
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('cats/cat_profile.html')
    else:
        print(form.errors)
    return render(request, 'cats/cat_profile.html', {'form': form})
    
def search(request):
    errormsg=""
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if CatProfile.objects.get(query):
            current_cat=request.cid
            cat=CatProfile.objects.get(cat=current_cat)
            breed=cat.breed
            price_range=cat.price_range
            friendliness=cat.friendliness
            tidiness=cat.tidiness
            fussiness=cat.fussiness
            description=cat.description
            cat_info = {'breed':breed,'price_range':price_range,'friendliness':friendliness,'tidiness':tidiness,'fussiness':fussiness,'description':description}
        else:
            errormsg="No matched cat founded."
    return render(request, 'cats/cat_profile.html', cat_info, errormsg)
