from django.conf.urls import url
from catalog.views import MenuList

from . import views

urlpatterns = [
    #url('', views.index, name='index'),
    url(r'^$', MenuList.as_view()),
]
