from django import forms

from StockApp.models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = {'name', 'price', 'status', 'issues'}


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = {'name', 'price', 'status', 'issues'}


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = {'name', 'price', 'status', 'issues'}
