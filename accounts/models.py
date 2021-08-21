from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.fields import BooleanField


class UserManager(BaseUserManager):

    def create_user(self,first_name,last_name,idcart,phone,email,address,shift,password,date):
             
        if not password:
            raise ValueError('plz password')        
    




        user=self.model(email=self.normalize_email(email),first_name=first_name,last_name=last_name,
        idcart=idcart,phone=phone,address=address,shift=shift,password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,idcart,phone,email,address,shift,password,date):
        user=self.create_user(first_name,last_name,idcart,phone,email,address,shift,password,date)
        user.is_admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    shift_status=((' A شیفت ',' A شیفت '),(' B شیفت ',' B شیفت '),
                (' C شیفت ',' C شیفت '),

    )
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    idcart=models.CharField(max_length=10,unique=True)
    phone=models.CharField(max_length=11)
    email=models.EmailField(blank=True)
    address=models.CharField(max_length=250)
    shift=models.CharField(max_length=10,choices=shift_status,blank=True,null=True)
    date=models.DateTimeField(null=True,blank=True)
    
    
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_authe=models.BooleanField(default=True)
    is_manager=models.BooleanField(default=False)
    
    USERNAME_FIELD='idcart'
    REQUIRED_FIELDS=['first_name','last_name','phone','email','address','shift','date']
    object=UserManager()

    def __str__(self):
        return self.first_name


    def has_perm(self, perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin  
    
