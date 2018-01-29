from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Reservation

# Create your views here.
class SmsView(TemplateView):
    template_name = 'reservation/index.html'

class ReservationsListView(ListView):
    model = Reservation

class ReservationsDetaileView(DeleteView):
    model = Reservation

class ReservationsCreateView(SuccessMessageMixin, CreateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'party_size', 'time']
    success_message = 'Your Reservation has been taken successfully'

class ReservationsUpdateView(UpdateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'party_size', 'time' ]
    success_message = 'You have updated/edited your reservation, Thank You'

class ReservationsDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('list_reservations')
