from django import forms

class RestoSearch(forms.Form):
	restaurants_open = forms.CharField(label='Restaurants open', max_length=100)