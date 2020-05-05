from django.shortcuts import render, redirect
from .models import Time

# Create your views here.

#HOME
def home(request):
	return render(request, "home.html", {})

#NEWPAGE
def appointment(request):
	return render(request, "newpage.html", {})

#ABOUT
def schedules(request):
	return render(request, "about.html", {})

			