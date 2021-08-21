from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model as user_model
from accounts.models import User
from django.db.models.fields import CharField
from django.urls import reverse
User=user_model()

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
    report=models.TextField(verbose_name='گزارش')
    date=models.DateTimeField( verbose_name='تاریخ ثبت')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نام کاربری')
    shift=models.CharField(max_length=50,choices=shift_status,verbose_name='شیفت',null=True)
    acepet=models.CharField(max_length=30,choices=acepet_status,default='تایید نشده')
    slug=models.SlugField(max_length=200,unique_for_date='date')
    

    def get_absolute_url(self):
        return reverse('net:detailreport',args=[self.slug,self.pk])

    def __str__(self):
        return '{} {}'.format(self.subject, self.user)