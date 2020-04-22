from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import *


@admin.register(Desktop, Laptop, Mobile)
class ViewAdmin(ImportExportModelAdmin):
    pass
