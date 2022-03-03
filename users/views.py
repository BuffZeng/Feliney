from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request, 'users/index.html')
    return response

def personal_info(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Rohan'}
    print(request.method)
    print(request.user)
    context_dict = {'visits': request.session['visits']}
    return render(request, 'users/indexo.html', context=context_dict)

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