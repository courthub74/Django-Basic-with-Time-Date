from django import forms
from .models import Time

class TimeForm(forms.ModelForm):
	class Meta:
		model = Time
		fields = ["first", "last", "coach", "focus", "date", "start", "end", "location", "facility", "address", "city", "state", "zipcode"]