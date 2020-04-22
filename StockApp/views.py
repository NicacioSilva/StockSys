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


def add_device(request, cls, item, item_url):
    if request.method == 'POST':
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect(item_url)
    else:
        form = cls()
        context = {
            'form': form,
            'header': item,
        }
        return render(request, 'add_new.html', context)


def add_laptop(request):
    return add_device(request, LaptopForm, 'laptop', 'show_laptops')


def add_desktop(request):
    return add_device(request, DesktopForm, 'desktop', 'show_desktops')


def add_mobile(request):
    return add_device(request, MobileForm, 'mobile', 'show_mobiles')


def edit_device(request, pk, model, cls, item_type, item_url):
    item = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(item_url)

    else:
        form = cls(instance=item)
        context = {
            'form': form,
            'header': item_type,
        }
        return render(request, 'edit_item.html', context)


def edit_laptop(request, pk):
    return edit_device(request, pk, Laptop, LaptopForm, 'laptop', 'show_laptops')


def edit_desktop(request, pk):
    return edit_device(request, pk, Desktop, DesktopForm, 'desktop', 'show_desktops')


def edit_mobile(request, pk):
    return edit_device(request, pk, Mobile, MobileForm, 'mobile', 'show_mobiles')


def delete_laptop(request, pk):
    Laptop.objects.filter(id=pk).delete()
    return redirect('show_laptops')


def delete_desktop(request, pk):
    Desktop.objects.filter(id=pk).delete()
    return redirect('show_desktops')


def delete_mobile(request, pk):
    Mobile.objects.filter(id=pk).delete()
    return redirect('show_mobiles')
