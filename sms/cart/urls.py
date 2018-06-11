from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<menu_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<menu_id>\d+)/$', views.cart_remove, name='cart_remove'),

    # url(r'^process/$', views.payment_process, name='process'),
]
# url(r'^(?P<slug>[-\w]+)/$', MenuDetailView.as_view(), name='menu_detail'),
