from sms import celery_app
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Reservation
from django.utils import timezone
from .tasks import removing_old_res
import arrow
import os



class ReservationListView(ListView):
    model = Reservation

    removing_old_res()


class ReservationDetailView(DetailView):
    model = Reservation


class ReservationCreateView(SuccessMessageMixin, CreateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'party_size', 'comments', 'time']
    success_message = 'Your Reservation has been taken successfully'


class ReservationUpdateView(SuccessMessageMixin, UpdateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'party_size', 'time' ]
    success_message = 'You have updated/edited your reservation, Thank You'

class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('list_reservation')
