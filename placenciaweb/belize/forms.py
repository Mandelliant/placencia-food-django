from django import forms
from .models import Resto


#gotta fix the CharField argument Search

class SearchForm(forms.Form):
    search_field = forms.CharField('Search', strip=True)


'''
class RestoSearch(forms.ModelForm):
	class Meta:	
		model = Resto
		fields = ('title', 'description', 'opening_hour', 'closing_hour')
'''




	#restaurants_open = forms.CharField(label='Restaurants open', max_length=100)