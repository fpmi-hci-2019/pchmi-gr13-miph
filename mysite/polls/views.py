from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.<a href='/accounts/login'>Login</a><a href='/accounts/logout'>Logout</a>")
