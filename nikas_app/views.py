from django.shortcuts import render
from django.http import HttpResponse


def view_name(request):
    return HttpResponse('Nikas 1st HM_Django with an empty link')

def view_name1(request):
    return HttpResponse('Nikas 2nd HM_Django with http://127.0.0.1:8000/acricles link')

def view_name2(request):
    return HttpResponse('Nikas 3rd HM_Django with http://127.0.0.1:8000/acrticles/archive link')

def view_name3(request):
    return HttpResponse('Nikas 4th HM_Django with http://127.0.0.1:8000/users link')
# Create your views here.
