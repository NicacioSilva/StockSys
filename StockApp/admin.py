from django.contrib import admin

from StockApp.models import *


@admin.register(Desktop, Laptop, Mobile)
class ViewAdmin(admin.ModelAdmin):
    pass
