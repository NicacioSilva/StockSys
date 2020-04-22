from django.conf.urls import url

from StockApp.views import *

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^show_laptops$', show_laptops, name='show_laptops'),
    url(r'^show_desktops$', show_desktops, name='show_desktops'),
    url(r'^show_mobiles$', show_mobiles, name='show_mobiles'),
]
