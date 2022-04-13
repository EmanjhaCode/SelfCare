from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ['id','title','image','paragraph1','paragraph2','paragraph3']

@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin):
    list_display = ['id','title','image','paragraph1','paragraph2','paragraph3']


@admin.register(Products)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ['id','title','image','paragraph1','paragraph2','paragraph3']

@admin.register(Programs)
class ProgramsAdmin(ImportExportModelAdmin):
    list_display = ['id','title','image','paragraph1','paragraph2','paragraph3']

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ['id','name','email','no','msg']
