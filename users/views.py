from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request, 'users/indexo.html')
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
    response = render(request, 'users/upload_photos.html')
    return response

def login(request):
    return render(request, 'users/login.html')

def home_page(request):
    return render(request,'users/index.html')

def edit_user(request):
    return render(request,'users/edit_info.html')

def add_cat(request):
    return render(request,'users/add_cat.html')