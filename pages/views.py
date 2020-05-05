from django.shortcuts import render, redirect
from .models import Time
from .forms import TimeForm
from django.contrib import messages

# Create your views here.

#HOME
def home(request): 
	return render(request, "home.html", {})

#NEWPAGE
def appointment(request):
	if request.method == 'POST':
		form = TimeForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Appointment Has Been Added!'))
			return redirect('schedules')
		else:
			messages.success(request, ('Seems Like There Was An Error...'))
			return render(request, 'newpage.html', {})
	else:
		return render(request, 'newpage.html', {})

#ABOUT
def schedules(request):
	all_appointments = Time.objects.all 
	#schedules = ['1','2','3','4']
	return render(request, "about.html", {'all_appointments': all_appointments}) # Passing in all_appointments as all_appointments

			