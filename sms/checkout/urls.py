from django.conf.urls import url
from . import views

app_name = "checkout"

urlpatterns = [
    url(r'^address/$', views.get_address, name='checkout_form'),

    ]
