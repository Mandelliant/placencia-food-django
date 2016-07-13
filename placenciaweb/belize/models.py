import datetime
from django.db import models
from django.utils import timezone
i = datetime.datetime.now()

class Restaurant(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField()
	opening_hour = models.TimeField(auto_now=False, auto_now_add=False, null=True)
	closing_hour = models.TimeField(auto_now=False, auto_now_add=False, null=True)
	days_open = models.TextField(blank=True)

	def is_open_today(self, day):
		open_days = [monday, tuesday, wednesday, thursday, friday, saturday, sunday].lower()
		if %i.day in open_days
	
