from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Reservation

# Create your views here.


class ReservationListView(ListView):
    model = Reservation

class ReservationDetailView(DetailView):
    model = Reservation

class ReservationCreateView(SuccessMessageMixin, CreateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'party_size', 'time']
    success_message = 'Your Reservation has been taken successfully'

class ReservationUpdateView(UpdateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'party_size', 'time' ]
    success_message = 'You have updated/edited your reservation, Thank You'

class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('list_reservations')
