from sms import celery_app
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
from timezone_field import TimeZoneField
from datetime import datetime
import arrow

class Reservation(models.Model):
    name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15)
    party_size = models.CharField(max_length=10)
    comments = models.TextField(max_length=255, blank=True)
    time = models.DateTimeField(default=datetime.now)
    time_zone = TimeZoneField(default='GMT')

    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['time']


    def __str__(self):
        return ('Reservations {0} - {1}'.format(self.pk, self.name))

    def get_absolute_url(self):
        return reverse('view_reservation', args=[str(self.id)])

    def clean(self):
        reservation_time = arrow.get(self.time, self.time_zone.zone)

        if reservation_time < arrow.utcnow():
            raise ValidationError("You cannot book a Reservation for the Past!, Please check your time. ")

    def schedule_reminder(self):
        reservation_time = arrow.get(self.time, self.time_zone)
        reminder_time = reservation_time.replace(minutes=-settings.REMINDER_TIME)

        from .tasks import send_sms_reminder
        result = send_sms_reminder.apply_async((self.pk,), eta=reminder_time)

        return result.id


    def save(self, *args, **kwargs):
        if self.task_id:
            celery_app.control.revoke(self.task_id)

        super(Reservation, self).save(*args, **kwargs)

        self.task_id = self.schedule_reminder()

        super(Reservation, self).save(*args, **kwargs)
