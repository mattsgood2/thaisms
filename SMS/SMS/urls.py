"""SMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

### will not need below once updated to django 2.0 ##
from django.conf.urls import include, url
#########################################
from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'home.html'), name='home'),
    url(r'^reservation/', include('reservation.urls')),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^checkout/', include('checkout.urls')),
    url(r'^payment/', include('payment.urls')),
    path('takeouts/', include('takeouts.urls')),
    url(r'^api/reservation/', include('reservation.api.urls', namespace='api-reservation')),
    url(r'^admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)



urlpatterns += staticfiles_urlpatterns()
