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

    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name='edit_laptop'),
    url(r'^edit_desktop(?P<pk>\d+)$', edit_desktop, name='edit_desktop'),
    url(r'^edit_mobile(?P<pk>\d+)$', edit_mobile, name='edit_mobile'),

    url(r'^delete_laptop/(?P<pk>\d+)$', delete_laptop, name='delete_laptop'),
    url(r'^delete_desktop(?P<pk>\d+)$', delete_desktop, name='delete_desktop'),
    url(r'^delete_mobile(?P<pk>\d+)$', delete_mobile, name='delete_mobile'),
]
