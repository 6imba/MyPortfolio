from django.urls import path
from . import views

urlpatterns = [
        path('education', views.education, name='educations'),
        path('skill', views.skill, name='skills'),
        path('certificate', views.certificate, name='certificate'),
]
