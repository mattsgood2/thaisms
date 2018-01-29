from django.conf.urls import url

from .views import SmsView, ReservationListView, ReservationCreateView, ReservationUpdateView, ReservationDetailView, ReservationDeleteView

urlpatterns = [
    url(r'^$', SmsView.as_view(), name=None),

    url(r'^$', ReservationListView.as_view(), name='list'),
    url(r'^/(?P<pk>[0-9]+)$', ReservationDetailView.as_view(), name='detail'),

    url(r'^new/$', ReservationCreateView.as_view(), name='new_reservation'),
    url(r'^/(?P<pk>[0-9]+)/edit$', ReservationUpdateView.as_view(), name='update_reservation'),
    url(r'^/(?P<pk>[0-9]+)/delete$', ReservationDeleteView.as_view(), name='delete_reservation'),


]
