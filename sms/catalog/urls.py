from django.conf.urls import url
from .views import (MenuListView,
                    MenuDetailView,
                    )

from catalog import views


#app_name = 'catalog'
urlpatterns = [
    #url('', views.index, name='index'),
    url(r'^$', MenuListView.as_view(), name='menulist'),
    url(r'^(?P<pk>[0-9]+)$', MenuDetailView.as_view(), name='menu_details'),
    #url(r'^(?P<slug>[-\w]+)/$', MenuDetailView.as_view(), name='menu'),
    #url(r'^list/$', ReservationListView.as_view(), name='list_reservation'),
]
