from django.db import models

class Resto(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField()
	opening_hour = models.TimeField(auto_now=False, auto_now_add=False, null=True)
	closing_hour = models.TimeField(auto_now=False, auto_now_add=False, null=True)
	days_open = models.TextField(blank=True)

	'''
	mon_open = models.TextField(blank=True)
	tue_open = models.TextField(blank=True)
	wed_open = models.TextField(blank=True)
	thu_open = models.TextField(blank=True)
	fri_open = models.TextField(blank=True)
	sat_open = models.TextField(blank=True)
	sun_open = models.TextField(blank=True)
	'''