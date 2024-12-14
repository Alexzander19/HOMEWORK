from django.contrib import admin

# Register your models here.

from .models import Interested, Services

admin.site.register(Services)
admin.site.register(Interested)
