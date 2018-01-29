from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

#def welcome_to_films(request):
    #return render(request, 'home.html')

class SmsView(TemplateView):
    template_name = 'home.html'
