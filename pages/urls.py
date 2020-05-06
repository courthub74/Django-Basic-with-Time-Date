from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('schedules/', views.schedules, name='schedules'),
    path('edit/<list_id>', views.edit, name='edit' )
    
]
