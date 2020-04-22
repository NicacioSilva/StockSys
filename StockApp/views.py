from django.shortcuts import render, redirect, get_object_or_404

from StockApp.models import *
from StockApp.forms import *


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


def add_device(request, cls, item):
    if request.method == 'POST':
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        context = {
            'form': form,
            'header': item,
        }
        return render(request, 'add_new.html', context)


def add_laptop(request):
    return add_device(request, LaptopForm, 'laptop')


def add_desktop(request):
    return add_device(request, DesktopForm, 'desktop')


def add_mobile(request):
    return add_device(request, MobileForm, 'mobile')


def edit_device(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_laptop(request, pk):
    return edit_device(request, pk, Laptop, LaptopForm)

def edit_desktop(request, pk):
    return edit_device(request, pk, Laptop, LaptopForm)

def edit_mobile(request, pk):
    return edit_device(request, pk, Laptop, LaptopForm)
