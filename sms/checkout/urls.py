from django.conf.urls import url
from . import views

app_name = "checkout"

urlpatterns = [
    url(r'^$', views.checkout, name='checkout'),

    ]
