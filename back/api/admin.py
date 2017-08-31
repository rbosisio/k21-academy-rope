from django.contrib import admin
from api.models import *

# Register your models here.

class DreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'medical_approved', 'parental_approved', 'status')
    list_filter = ('status',)

admin.site.register(Dream, DreamAdmin)