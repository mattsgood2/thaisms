from django.conf.urls import url
from .views import ReservationRudView, ReservationListView

app_name = 'api'
urlpatterns = [
    url(r'^$', ReservationListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ReservationRudView.as_view(), name='res-rud'),
]
