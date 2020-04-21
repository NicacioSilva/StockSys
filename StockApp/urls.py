from django.conf.urls import url

from StockApp.views import index

urlpatterns = [

    url(r'^$', index, name='index')

]
