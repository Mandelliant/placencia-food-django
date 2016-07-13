from django.shortcuts import render
from django.http import Http404
from django.shortcuts import HttpResponse
from belize.models import Resto
from django.core.exceptions import *
from django.db.models import Q




def index(request):
	return render(request, 'belize/index.html')



def search(request):
    form = SearchForm(request.GET)
    results = []  # Set results to an empty list
    if form.is_valid():
       needle = form.cleaned_data['search_field'].capitalize()
       results = Restaurant.objects.filter(Q(days_open__startswith='{},'.format(needle)) |
                 Q(days_open__endswith=',{}'.format(needle)) |
                 Q(days_open__contains=',{},'.format(needle)) |
                 Q(days_open='{},'.format(needle)) |
                 Q(days_open='{}'.format(needle)))
    return render(request, 'search.html', {'results': results, 'form': form})


def restaurant_detail(request, id):
	try:
		restaurant = Restaurant.objects.get(id=id)
	except Resto.DoesNotExist:
		raise Http404('This restaurant does not exist')
	return render(request, 'belize/restaurant_detail.html', {
		'restaurant': restaurant,
		})
