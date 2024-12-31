from django.contrib import admin

from users.models import User

# from users.models import User

from .models import Hall,Movie,Session, Ticket

# Register your models here.

admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Session)
# для отладки все же добавлю
admin.site.register(Ticket)
admin.site.register(User)

