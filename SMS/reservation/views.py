from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Reservation
#from datetime import datetime
from django.utils import timezone
import arrow
import os


#now = timezone.now()
# Create your views here.
#client = Client(account_sid, auth_token)
account_sid = os.environ['MY_TWILIO_ACCOUNT_SID']
auth_token = os.environ['MY_TWILIO_AUTH_TOKEN']

class ReservationListView(ListView):
    model = Reservation

    old_reservation_delete = Reservation.objects.filter(time__lt = timezone.now())
    for r in old_reservation_delete:
        old_reservation_delete.delete()
    reservation = Reservation.objects.all()


class ReservationDetailView(DetailView):
    model = Reservation


class ReservationCreateView(SuccessMessageMixin, CreateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'party_size', 'comments', 'time']
    success_message = 'Your Reservation has been taken successfully'

    #def form_valid(self, form):
    #    form.send_sms_confirm()
    #    def send_print():
    #        print("TITITITITITITITI")

    #    return super().form_valid(form)
    #if form_valid():
    #    print ("tit")
    #client = Client(account_sid, auth_token)
    #message = client.messages.create(
    #    body = "worked like this",
    #    to =os.environ['MY_PHONE_NUMBER'], #Should be reservation.phone_number,
    #    from_ = os.environ['MY_TWILIO_NUMBER'],
    #    )




class ReservationUpdateView(SuccessMessageMixin, UpdateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'party_size', 'time' ]
    success_message = 'You have updated/edited your reservation, Thank You'

class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('list_reservation')
