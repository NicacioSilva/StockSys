from django.conf.urls import url

from StockApp.views import *

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^show_laptops$', show_laptops, name='show_laptops'),
]
