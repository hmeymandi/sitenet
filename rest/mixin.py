from django.http.response import Http404
from rest.models import *


class FieldMixin():
    
    def dispatch(self, request, *args, **kwargs):
          
        if self.request.user.is_admin or self.request.user.is_manager  or self.request.user.is_nazer:
               
               self.fields=['user','user1','type','time1','time2','accept']
        elif self.request.user.is_authe or self.request.user.is_active:

               self.fields=['user','type','time1','time2','accept']
        else:
            raise Http404
        return super().dispatch(request,*args,**kwargs)

class FormValid():
    def form_valid(self,form):
        if self.request.user.is_admin:
            form.save()

        else:
            form.instance.user1=self.request.user
                              
            self.obj=form.save()
            if not self.obj.accept==['تایید سرپرست','تایید ناظر','تایید سرپرست']:
                self.obj.accept='در دست بررسی'

        return super().form_valid(form)



class AccsesMixin():
    # user=is_active is_admin is_authe  is_manager is_nazer
    def dispatch(self, request,pk, *args, **kwargs):
        update=Restmodel.objects.get(pk=pk)
        if update.user1==request.user or update.accept =='در دست بررسی' or  request.user.is_admin or \
            request.user.is_manager  :
            return super().dispatch(request,pk,*args,**kwargs)

        if request.user.is_nazer and update.accept =='تایید سرپرست':
               
            return super().dispatch(request,pk,*args,**kwargs)

        else:
            raise Http404 ('شما دسترسی به این بحش را ندارید')
