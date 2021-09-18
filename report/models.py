from datetime import date, datetime, time,timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model as user_model
from accounts.models import User
from django.db.models.fields import CharField
from django.urls import reverse
from jalali_date import datetime2jalali,date2jalali
from django.contrib.contenttypes.fields import GenericRelation
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime








User=user_model()




class Informationmodel(models.Model):
    class Meta:
        verbose_name='اطلاعات'
        verbose_name_plural='اطلاعات'
        ordering=['position']

    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.CharField(max_length=100,unique=True)
    status=models.BooleanField(default=True,verbose_name='نمایش')
    position=models.IntegerField(verbose_name='موقیعت')

    def __str__(self) -> str:
        return self.title



class Reportmodel(models.Model):
    class Meta:
        verbose_name='گزارش'
        verbose_name_plural='گزارش'
       
    acepet_status=(('تایید نشده','تایید نشده'), 
                    ('تایید سر شیفت','تایید سر شیفت'),
                    ('تایید نهایی','تایید نهایی'),
    
    )

    shift_status=(('شیفت A','شیفت A'),
    ('شیفت B','شیفت B'),
    ('شیفت C','شیفت C'),)

    subject=models.CharField(max_length=100,verbose_name='موضوع')
    categ=models.ManyToManyField(Informationmodel,verbose_name='دسته بندیُ',related_name='info')
    report=models.TextField(verbose_name='گزارش')
    date=models.DateTimeField(default=timezone.now,verbose_name='تاریخ ثبت',)
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نام کاربری')
    shift=models.CharField(max_length=50,choices=shift_status,verbose_name='شیفت',null=True)
    acepet=models.CharField(max_length=30,choices=acepet_status,default='تایید نشده',verbose_name='وضیعت')
    slug=models.SlugField(max_length=200,unique_for_date='date')


    
    def get_absolute_url(self):
        return reverse("net:listreport")
    
    def get_absolute_url1(self):
        return reverse('net:detailreport',args=[self.slug,self.pk])

  


    def __str__(self):
        return '{} {}'.format(self.subject, self.user)

    
 
    
    def persian_number(self):
        time2str=str(datetime2jalali(self.date))
        number={
            '0':'۰',
            '1':'۱',
            '2':'۲',
            '3':'۳',
            '4':'۴',
            '5':'۵',
            '6':'۶',
            '7':'۷',
            '8':'۸',
            '9':'۹',
       }

        for i,j in number.items():
            time2str=time2str.replace(i,j)
            
        return time2str

   