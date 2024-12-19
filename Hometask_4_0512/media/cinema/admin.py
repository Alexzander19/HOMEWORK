from django.contrib import admin

from .models import Hall,Movie,Session

# Register your models here.

admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Session)

