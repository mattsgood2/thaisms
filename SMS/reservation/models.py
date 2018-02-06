from SMS import celery_app
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
from timezone_field import TimeZoneField

import arrow

class Reservation(models.Model):
    name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15)
    party_size = models.CharField(max_length=10)
    comments = models.TextField(max_length=255)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='GMT')

    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ('Reservations {0} - {1}'.format(self.pk, self.name))

    def get_absolute_url(self):
        return reverse('view_reservation', args=[str(self.id)])

    def clean(self):
        reservation_time = arrow.get(self.time, self.time_zone.zone)

        if reservation_time < arrow.utcnow():
            raise ValidationError("You cannot book a Reservation for the Past!, Please check you time. ")
