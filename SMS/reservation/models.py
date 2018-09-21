from sms import celery_app
from django.conf import settings
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db import models
from twilio.rest import Client
from timezone_field import TimeZoneField
from datetime import datetime
import os
import arrow


account_sid = os.environ['MY_TWILIO_ACCOUNT_SID']
auth_token = os.environ['MY_TWILIO_AUTH_TOKEN']

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
        return reverse('reservations:view_reservation', args=[str(self.id)])

    def clean(self):
        reservation_time = arrow.get(self.time, self.time_zone.zone)

        if reservation_time < arrow.utcnow():
            raise ValidationError("You cannot book a Reservation for the Past!, Please check your time. ")

        client = Client(account_sid, auth_token)

        confirm_booking = arrow.get(self.time, self.time_zone)
        body = "CONFIRMED BOOKING FOR\n '{0}'\n DATE & TIME '{1}'\n PARTY OF '{2}'\n MANY THANKS. ".format(self.name, confirm_booking.format('DD-MM-YYYY @ HH:mm a '), self.party_size, confirm_booking.format('DD-MM-YYYY HH:mm a '))
        message = client.messages.create(
            body = body,
            to =os.environ['MY_PHONE_NUMBER'], #Should be reservation.phone_number,
            from_ = os.environ['MY_TWILIO_NUMBER'],
            )

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
