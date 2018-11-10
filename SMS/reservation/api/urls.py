from django.conf.urls import url
from .views import ReservationRudView

app_name = 'api'
urlpatterns = [
    url(r'^(?P<pk>\d+)$', ReservationRudView.as_view(), name='res-rud'),
]
