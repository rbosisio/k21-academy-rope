from django.contrib import admin
from api.models import *
from django import forms

# Register your models here.

class DreamAdmin(admin.ModelAdmin):
    list_display = ('dreamer_name', 'dream_nickname', 'local', 'provisional_date', 'status')
    list_filter = ('status', 'local', 'provisional_date')

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ('name', 'email','assignment', 'status')
	list_filter = ('status', 'assignment')

class PartnerAdmin(admin.ModelAdmin):
	list_display = ('company_name', 'contact_name', 'telephone', 'money_help', 'service_help', 'has_specific_dream', 'status')
	list_filter = ('status', 'money_help', 'service_help', 'has_specific_dream')

class DaysTimesAdmin(admin.ModelAdmin):
	list_display = ('day', 'time')

admin.site.register(Dream, DreamAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(AvailableDaysTimes, DaysTimesAdmin)