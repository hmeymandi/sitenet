from django.forms import fields
from .models import Restmodel
from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime




class Restform(forms.ModelForm):
    class Meta:
        model=Restmodel
        fields=['user','user1','type','time1','time2','accept']

   