from django.conf.urls import url

from .views import SmsView, ReservationsListView, ReservationsCreateView, ReservationsUpdateView, ReservationsDetaileView

urlpatterns = [
    url(r'^$', SmsView.as_view(), name=None),

    url(r'^$', ReservationsListView.as_view(), name='list_appointments'),
    url(r'^/(?P<pk>[0-9]+)$', ReservationsDetailView.as_view(), name='view_appointment'),

    url(r'^/new$', ReservationsCreateView.as_view(), name='new_reservation'),
    url(r'^/(?P[0-9]+)/update$', ReservationsUpdatView.as_view(), name='update_reservation'),
    url(r'^/(?P[0-9]+)/delete$', ReservationsDeleteView.as_view(), name='delete_reservation'),


]
