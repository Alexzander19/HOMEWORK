from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

# from users.models import User

from .models import Hall,Movie,Session, Ticket

# Register your models here.


admin.site.site_header = "Управление домашним кинотеатром"
admin.site.site_title = "Админка Домашнего кинотеатра"
admin.site.index_title = "Добро пожаловать в Домашний кинотеатр"

# admin.site.register(Hall)
# admin.site.register(Movie)
# admin.site.register(Session)
# для отладки все же добавлю
admin.site.register(Ticket) # Эта модель меня и в своем виде устраивает
# admin.site.register(User)



@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
  list_display = ('name', 'capacity')  # Поля для отображения в списке
  ordering = ('capacity',)  # Сортировка записей


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
  list_display = ('title', 'genre', 'duration')  # Поля для отображения в списке
  list_filter = ('genre', 'release_date')  # Фильтры в правой части админки
  search_fields = ('title', 'description')  # Поля для поиска
  ordering = ('release_date',)  # Сортировка записей

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hall', 'show_time')  # Поля для отображения в списке
    list_filter = ('movie', 'hall')  # Фильтры в правой части админки
    search_fields = ('movie__title',)  # Поля для поиска ПО ПОЛЯМ FOREIGNKEY
    ordering = ('hall',)  # Сортировка записей
    
# class User(AbstractUser):
#   firstname = models.CharField(max_length=100)
#   lastname = models.CharField(max_length=100)

#   def __str__(self):
#     return self.username

# username_validator = UnicodeUsernameValidator()

#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         unique=True,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[username_validator],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#     )
#     first_name = models.CharField(_("first name"), max_length=150, blank=True)
#     last_name = models.CharField(_("last name"), max_length=150, blank=True)
#     email = models.EmailField(_("email address"), blank=True)
#     is_staff = models.BooleanField(
#         _("staff status"),
#         default=False,
#         help_text=_("Designates whether the user can log into this admin site."),
#     )
#     is_active = models.BooleanField(
#         _("active"),
#         default=True,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )
#     date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

#     objects = UserManager()

#     EMAIL_FIELD = "email"
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]

@admin.register(User)
class UserAdmin(UserAdmin):
  list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
  fieldsets = UserAdmin.fieldsets + (
    ('Дополнительная информация', {'fields': ('firstname', 'lastname')}),
) #+ (('Дата регистрации, активен или нет', {'fields': ('is_active',)}),)
#   это уже есть в fieldsets базового класса UserAdmin
    


#   @admin.register(Movie)
# class TaskAdmin(admin.ModelAdmin):
#   list_display = ('title', 'status', 'due_date', 'project')  # Поля для отображения в списке
#   list_filter = ('status', 'project')  # Фильтры в правой части админки
#   search_fields = ('title', 'description')  # Поля для поиска
#   ordering = ('due_date',)  # Сортировка записей
#   fieldsets = UserAdmin.fieldsets + (
#     ('Дополнительная информация', {'fields': ('firstname', 'lastname')}),
#   )