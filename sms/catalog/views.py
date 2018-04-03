from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Menu
# Create your views here.
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the Menu index.")

class MenuList(ListView):
    model = Menu
