from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def weather(request):
    return render(request, 'weather/weather.html')

    
