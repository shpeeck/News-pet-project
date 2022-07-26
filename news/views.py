from django.shortcuts import render,  Http404
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'news/index.html')

def foo(request):
    return render(request, 'news/index_test.html')