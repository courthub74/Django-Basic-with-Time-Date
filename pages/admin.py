from django.contrib import admin
from .models import Time

# Register your models here.
# BELOW registers the Time class through admin area

admin.site.register(Time)


# after this do:
	# python manage.py makemigrations
	# python manage.py migrate