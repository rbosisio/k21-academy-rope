from django.contrib import admin
from api.models import *
from django import forms

# Register your models here.

class DreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'medical_approved', 'parental_approved', 'status')
    list_filter = ('status',)

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ('name', 'email','assignment', 'status')
	list_filter = ('status',)

class DaysTimesAdmin(admin.ModelAdmin):
	list_display = ('day', 'time')

admin.site.register(Dream, DreamAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(AvailableDaysTimes, DaysTimesAdmin)