from django import forms
from django.forms.forms import Form
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UsercreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['first_name','last_name','idcart','phone','email','address','shift','date','password']

    def clean_password2(self):
        data=self.cleaned_data
        if data['password2'] and data['password1'] and data['password2'] !=data['password1']:
            raise forms.ValidationError('plz check password')
        return data['password2']


    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user    

class UserchangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField

    class Meta:
        model=User
        fields=['first_name','last_name','idcart','phone','email','address','shift','date','password']

    def clean_password(self):
        return self.initial['password']

class Userloginform(forms.Form):
    idcart=forms.CharField()
    password=forms.CharField(label='رمز عبور',widget=forms.PasswordInput)