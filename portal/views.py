from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# common login rendering template
def login(request):
    return HttpResponse("Login page")