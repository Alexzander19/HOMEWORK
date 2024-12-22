from django.contrib import admin

from .models import Hall,Movie,Session, Ticket

# Register your models here.

admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Session)
# для отладки все же добавлю
admin.site.register(Ticket)

