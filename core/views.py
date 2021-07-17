from django.shortcuts import render

# Create your views here.

def home(request):
    status = {'home':'active'}
    return render(request, 'core/home.html', status)

def contact(request):
    status = {'contact':'active'}
    return render(request, 'core/contact.html', status)