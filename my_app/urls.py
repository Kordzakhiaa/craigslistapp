from django.urls import path
from .views import home, new_search

app_name = 'my_app'

urlpatterns = [
    path('', view=home, name='home_page'),
    path('search/', view=new_search, name='new_search'),
]
