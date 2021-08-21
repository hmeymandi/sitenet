from django.http import request
from django.forms import forms
from django.shortcuts import redirect


class FieldMixin():

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_admin:
             self.fields=['subject','report','date','user','shift','slug','acepet']
        elif self.request.user.is_authe:
             self.fields=['subject','report','date','user','shift','slug','acepet']
        
        
        return super().dispatch(request, *args, **kwargs)
class FormValidMixin():
     def form_valid(self,form):
          if self.request.user.is_admin:
               form.save()
        
          else:
               self.obj=form.save(commit=False)
               self.obj.user=self.request.user
               self.obj.acepet='تایید نشده'
          return super().form_valid(form)