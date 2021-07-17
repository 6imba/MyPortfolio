from django.shortcuts import render

# Create your views here.
def education(request):
    status = {'education':'active'}
    return render(request, 'edu/education.html', status)

def skill(request):
    status = {'skill':'active'}
    return render(request, 'edu/skill.html', status)
