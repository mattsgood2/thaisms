from django.conf.urls import url

from . import views


app_name = 'cart'

urlpatterns = [
    url(r'^$', views.show_cart, name='show_cart')
    # #url('', views.index, name='index'),
    # url(r'^$', MenuListView.as_view(), name='menu_list'),
    # #url(r'^(?P<pk>[0-9]+)$', MenuDetailView.as_view(), name='menu_detail'),
    # url(r'^(?P<slug>[-\w]+)/$', MenuDetailView.as_view(), name='menu_detail'),

]
