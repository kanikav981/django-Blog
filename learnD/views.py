from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hey! It is my django first page")

def index(request):
    return render(request,'index.html')
