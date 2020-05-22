from django.shortcuts import render, redirect
from .models import Time
from .forms import TimeForm
from django.contrib import messages
from django.db.models import Q 

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
def delete(request, list_id):
	if request.method == 'POST':
		current_appointment = Time.objects.get(pk=list_id)
		current_appointment.delete()
		messages.success(request, ('Appointment Has Been Deleted...'))
		return redirect('schedules')
	else:
		messages.success(request, ('Nothing To See Here...'))
		return redirect('schedules')


#SEARCH
def search(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = Time.objects.all 
		for post in posts:
			queryset.append(post)
	return list(set(queryset))

	#all_appointments = Time.objects.all 
	#return render(request, "about.html", {'all_appointments': all_appointments})

#COMPLETE

	#Here you retrieve whats on the appointments list and
	#populate it to a created chart on the next page
			