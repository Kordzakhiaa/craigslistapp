import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from .models import *

URL = 'https://losangeles.craigslist.org/search/?query={}'


def home(request):
    return render(request, 'my_app/home.html')


def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    final_url = URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_title = soup.find_all('a', {'class': 'result-title'})
    
    context = {'search': search}
    return render(request, 'my_app/new_search.html', context)
