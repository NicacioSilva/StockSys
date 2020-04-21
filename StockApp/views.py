from django.shortcuts import render

from StockApp.models import *


def index(request):
    return render(request, 'index.html')


def show_laptops(request):
    # the functions's propose is to get all the laptop objects and show them on index page.
    items = Laptop.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'index.html', context)