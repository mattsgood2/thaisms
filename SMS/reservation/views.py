from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class SmsView(TemplateView):
    template_name = 'reservation/index.html'
