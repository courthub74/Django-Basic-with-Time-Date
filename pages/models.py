from django.db import models

#Create a Class here

class Time(models.Model):
	date = models.CharField(max_length=200)
	start = models.CharField(max_length=200)
	end = models.CharField(max_length=200)

	def __str__(self):
		return self.date



