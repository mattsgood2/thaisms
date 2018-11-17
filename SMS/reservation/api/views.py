# from django.contrib.auth.models import User
# from myapp.serializers import UserSerializer
from django.db import models
from django.db.models import Q

from reservation.models import Reservation
from rest_framework import generics, mixins
from .serializers import ReservationSerializer
# from rest_framework.permissions import IsAdminUser
######
# from rest_framework import filters

######

class ReservationListView(mixins.CreateModelMixin, generics.ListAPIView):
    # queryset = Reservation.objects.all()
    lookup_field  = 'pk'
    serializer_class = ReservationSerializer

    def get_queryset(self):
        qs = Reservation.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(name__contains=query)|Q(mobile_number__icontains=query))
        return qs

    # def get_queryset(self):
    #     return Reservation.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReservationRudView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Reservation.objects.all()
    lookup_field  = 'pk'
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.all()
