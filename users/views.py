from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request, 'users/indexo.html')
    return response

def personal_info(request):
    return render(request, 'users/index.html')

def all_coments(request):
    context_dict = {'visits': request.session['visits']}
    response = render(request, 'users/indexo.html', context=context_dict)
    return response

def edit_ratings(request):
    context_dict = {'visits': request.session['visits']}
    response = render(request, 'users/indexo.html', context=context_dict)
    return response

def upload_image(request):
    context_dict = {'visits': request.session['visits']}
    response = render(request, 'users/indexo.html', context=context_dict)
    return response

def login(request):
    return render(request, 'users/login.html')

def home_page(request):
    return render(request,'users/index.html')