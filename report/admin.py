from django.contrib import admin
from .models import *

@admin.register(Reportmodel)
class Reportadmin(admin.ModelAdmin):
    field=['user','shift','user']
    list_display=['user','shift','date']