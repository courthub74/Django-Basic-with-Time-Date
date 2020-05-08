from django.db import models

#Create a Class here
class Time(models.Model):
	first = models.CharField(max_length=200, blank=True, null=True)
	last = models.CharField(max_length=200, blank=True, null=True)
	coach = models.CharField(max_length=200, blank=True, null=True)
	focus = models.CharField(max_length=200, blank=True, null=True)
	date = models.CharField(max_length=200)
	start = models.CharField(max_length=200)
	end = models.CharField(max_length=200)
	location = models.CharField(max_length=200, blank=True, null=True)
	


	def __str__(self):
		return self.first



# when ADDING to existing model use (blank=True, null=True)

# makes it nullable

