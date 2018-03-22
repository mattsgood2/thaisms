from __future__ import absolute_import
from celery import shared_task
from django.conf import settings
from celery.task import periodic_task
from datetime import timedelta
from django.utils import timezone
#from celery.schedules import crontab
from twilio.rest import Client
import os
import environ
import arrow

from .models import Reservation

account_sid = os.environ['MY_TWILIO_ACCOUNT_SID']
auth_token = os.environ['MY_TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

@shared_task
def send_sms_reminder(reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
    except Reservation.DoesNotExist:
        return

    reservation_time = arrow.get(reservation.time, reservation.time_zone)
    body = "Hi you have a Reservation booked under the name {0} at {1} today ".format(reservation.name, reservation_time.format('h:mm a'))

    message = client.messages.create(
        body = body,
        to =os.environ['MY_PHONE_NUMBER'], #Should be reservation.phone_number,
        from_ = os.environ['MY_TWILIO_NUMBER'],
    )


@periodic_task(run_every=timedelta(seconds=1800))
def removing_old_res():
    old_reservation_delete = Reservation.objects.filter(time__lt = timezone.now())
    for r in old_reservation_delete:
        old_reservation_delete.delete()
    reservation = Reservation.objects.all()
