from django.shortcuts import render

# Create your views here.

def services(request):
    status = {'service':'active'}
    return render(request, 'serve/services.html', status)