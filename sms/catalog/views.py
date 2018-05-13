from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Menu
# Create your views here.
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the Menu index.")

class MenuListView(ListView):
    model = Menu
    #context_object_name = 'menu_page'

class MenuDetailView(DetailView):
    model = Menu
    
