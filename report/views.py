from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
from accounts.mixin import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.core.paginator import Paginator
from django.views.generic import CreateView

# Create your views here.
def listreport(request):
    #print(request.user.is_authe)
    report=Reportmodel.objects.all()
    paginator=Paginator(report,3)   
    pagenum=request.GET.get('page')
    page_obj=paginator.get_page(pagenum)
    context={'report':page_obj}

    return render(request,'listreport.html',context)


def detailreport(request,slug,pk):
    
    form=Reportmodel.objects.get(slug=slug,pk=pk)
    
    return render(request,'deatil.html',{'form':form})

class CreateReport(LoginRequiredMixin,FormValidMixin,FieldMixin,CreateView):
    model=Reportmodel
    #fields=['subject','report','date','user','shift','acepet','slug']
    template_name='reportform.html'
