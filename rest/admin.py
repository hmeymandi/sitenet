from django.contrib import admin
from .models import Restmodel

# Register your models here.

@admin.register(Restmodel)
class Restadmin(admin.ModelAdmin):
    fields=['user','user1','type','accept','time1','time2']
    list_filter=['accept']
    list_display=['user','user1','type','accept','time1','time2']
    
