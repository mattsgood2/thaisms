from django.conf.urls import url
from .views import (MenuList,
                    MenuDetailView,
                    )

from . import views

urlpatterns = [
    #url('', views.index, name='index'),
    url(r'^$', MenuList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', MenuDetailView.as_view(), name='views_details'),
    #url(r'^(?P<slug>[-\w]+)/$', MenuDetailView.as_view(), name='menu'),
]
