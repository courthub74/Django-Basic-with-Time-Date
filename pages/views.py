from django.shortcuts import render

# Create your views here.

#HOME
def home(request):
	return render(request, "home.html", {})

#ABOUT
def about(request):
	return render(request, "about.html", {})

#NEWPAGE
def newpage(request):
	return render(request, "newpage.html", {})			