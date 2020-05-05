from django.shortcuts import render, redirect
from .models import Time
from .forms import TimeForm
from django.contrib import messages

# Create your views here.

#HOME
def home(request):
	all_appointments = Time.objects.all 
	return render(request, "home.html", {'all_appointments': all_appointments})

#NEWPAGE
def appointment(request):
	return render(request, "newpage.html", {}) 

#ABOUT
def schedules(request):
	all_appointments = Time.objects.all 
	#schedules = ['1','2','3','4']
	return render(request, "about.html", {'all_appointments': all_appointments}) # Passing in all_appointments as all_appointments

			