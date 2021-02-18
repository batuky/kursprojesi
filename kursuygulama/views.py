from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'kursuygulama/index.html')

def about(request):
    return render(request,'kursuygulama/about.html')

def contact(request):
    return render(request,'kursuygulama/contact.html')
    
def register(request):
    return render(request,'kursuygulama/register.html')

def login(request):
    return render(request,'kursuygulama/login.html')