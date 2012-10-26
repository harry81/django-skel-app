from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = patterns('apps.goodprice.views',
                       (r'^$', 'index'),                       
                       )

