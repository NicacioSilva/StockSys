from django.shortcuts import render

from StockApp.models import *


def index(request):
    return render(request, 'index.html')


def show_laptops(request):
    # the functions's propose is to get all the laptop objects and show them on index page.
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptops'
    }
    return render(request, 'index.html', context)


def show_desktops(request):
    # the functions's propose is to get all the desktops objects and show them on index page.
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktops'
    }
    return render(request, 'index.html', context)


def show_mobiles(request):
    # the functions's propose is to get all the mobiles objects and show them on index page.
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobile'
    }
    return render(request, 'index.html', context)


