from django.shortcuts import render
from django.http import Http404
from django.shortcuts import HttpResponse
from belize.models import Resto
from django.core.exceptions import *

'''
def index(request):
	options = Resto.objects.exclude(mon_open=True, tue_open=True, wed_open=True, thu_open=True, fri_open=True, sat_open=True, sun_open=True)
	return render(request, 'belize/index.html', {
		'restaurants': options,

		})

'''

def index(request):
	return render(request, 'form.html')

def search(request):
	if request.method == 'POST':
		search_id=request.POST.get('textfield', None)
		try:
			available = Resto.objects.get(name = search_id)
        	#do something with user
			html = ("<H1>%s</H1>", available)
			return HttpResponse(html)
		except Resto.DoesNotExist:
			return HttpResponse("Please try another day")  
		else:
			return render(request, 'belize/form.html')


def restaurant_detail(request, id):
	try:
		restaurant = Resto.objects.get(id=id)
	except Resto.DoesNotExist:
		raise Http404('This restaurant does not exist')
	return render(request, 'belize/restaurant_detail.html', {
		'restaurant': restaurant,
		})