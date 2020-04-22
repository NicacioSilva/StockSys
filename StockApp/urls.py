from django.conf.urls import url

from StockApp.views import *


urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^show_laptops$', show_laptops, name='show_laptops'),
    url(r'^show_desktops$', show_desktops, name='show_desktops'),
    url(r'^show_mobiles$', show_mobiles, name='show_mobiles'),

    url(r'^add_laptop$', add_laptop, name='add_laptop'),
    url(r'^add_desktop$', add_desktop, name='add_desktop'),
    url(r'^add_mobile$', add_mobile, name='add_mobile'),

    url(r'^add_laptop$', add_laptop, name='add_laptop'),
    url(r'^add_desktop$', add_desktop, name='add_desktop'),
    url(r'^add_mobile$', add_mobile, name='add_mobile'),
]
