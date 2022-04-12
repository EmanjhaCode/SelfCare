from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(chat)
class chatAdmin(ImportExportModelAdmin):
    list_display = ['id','tag','patterns','responses']

@admin.register(bot_user)
class bot_userAdmin(ImportExportModelAdmin):
    list_display = ['user_id','user_res','bot_res']
