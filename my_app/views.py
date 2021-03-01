from django.shortcuts import render
from .models import *
from .parser import parser

URL = 'https://losangeles.craigslist.org/search/?query={}'
IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)

    context = {
        'search': search,
        'final_postings': parser(search),
    }
    return render(request, 'my_app/new_search.html', context)
