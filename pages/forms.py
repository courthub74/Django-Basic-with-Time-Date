from django import forms
from .models import Time

class TimeForm(forms.ModelForm):
	class Meta:
		model = Time
		fields = ["date", "start", "end"]