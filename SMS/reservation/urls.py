from django.conf.urls import url

from .views import SmsView, ReservationsCreateView, ReservationsDetaileView

urlpatterns = [
    url(r'^$', SmsView.as_view(), name=None),
     url(r'^/new$', ReservationsCreateView.as_view(), name='new_reservation'),
     url(r'^/(?P[0-9]+)/delete$', ReservationsDeleteView.as_view(), name='delete_reservation'),


]
