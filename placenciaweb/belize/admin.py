from django.contrib import admin

from .models import Resto

class RestoAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(Resto, RestoAdmin)
