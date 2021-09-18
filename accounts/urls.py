from django.urls import path,include
from . import views

app_name='account'
urlpatterns = [
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),

]