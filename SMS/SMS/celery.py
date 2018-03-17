#from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms.settings')

app = Celery('sms', broker='redis://localhost:6379/0')

app.config_from_object('django.conf:settings', namespace= 'CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

#app.conf.broker_url = 'redis://localhost:6379/0'
