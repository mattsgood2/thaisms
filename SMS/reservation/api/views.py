# from django.contrib.auth.models import User
# from myapp.serializers import UserSerializer
from reservation.models import Reservation
from rest_framework import generics
from .serializers import ReservationSerializer
# from rest_framework.permissions import IsAdminUser

class ReservationRudView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Reservation.objects.all()
    lookup_field  = 'pk'
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.all()
