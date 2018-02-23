from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
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
    except Reservation.DoesNotExits:
        return

    reservation_time = arrow.get(reservation.time, reservation.time_zone)
    body = "Hi you have a Reservation booked under the name {} at {0} today ".format(reservation.name, reservation_time.format('h:mm a'))

    message = client.messages.create(
        body = body,
        to =os.environ['MY_PHONE_NUMBER'], #Should be reservation.phone_number,
        from_ = os.environ['MY_TWILIO_NUMBER'],
    )
