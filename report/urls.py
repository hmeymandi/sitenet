from django.urls import path
from . import views

app_name='net'
urlpatterns = [

        path('listreport',views.listreport,name='listreport'),
        path('detailreport/<slug:slug>/<int:pk>',views.detailreport,name='detailreport'),
        path('reportform',views.CreateReport.as_view(),name='reportform'),

]