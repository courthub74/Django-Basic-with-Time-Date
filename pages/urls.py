from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('schedules/', views.schedules, name='schedules'),
    path('edit/<list_id>', views.edit, name='edit' ),
    path('delete/<list_id>', views.delete, name='delete'), #You don't need to make a delete.html but the url path is needed
    path('s/', views.schedules, name='search'),
    
]
