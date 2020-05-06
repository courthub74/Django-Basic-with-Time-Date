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


#EDIT
def edit(request, list_id):
	if request.method == 'POST':
		current_appointment = Time.objects.get(pk=list_id)
		form = TimeForm(request.POST or None, instance=current_appointment)
		if form.is_valid():
			form.save()
			messages.success(request, ('Appointment Has Been Edited!'))
			return redirect('schedules')
		else:
			messages.success(request, ('Seems Like There Was an Error...'))
			return render(request, 'edit.html', {})
	else:
		get_appointment = Time.objects.get(pk=list_id)
		return render(request, 'edit.html', {'get_appointment': get_appointment})


#DELETE

			