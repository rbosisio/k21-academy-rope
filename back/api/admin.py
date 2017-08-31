from django.contrib import admin
from api.models import *

# Register your models here.

class DreamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dream, DreamAdmin)