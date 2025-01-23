from django.db import models
from users.models import User

# Create your models here.

# verbose_name наследуется от родительских классов. 
# в классе Session Осуществляется поиск по полю movie.ForeignKey.

# Модель Movie (Фильм):
# Поля:
# title (название фильма).
# duration (длительность фильма в минутах).
# genre (жанр фильма).
# release_date (дата выхода фильма).


class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    title = models.CharField(max_length=200,verbose_name='Название')
    duration = models.IntegerField(verbose_name='Продолжительность')
    genre = models.CharField(max_length=50,verbose_name='Жанр')
    release_date = models.DateField(verbose_name='Дата выхода')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title[0:20] +', ' + self.genre[0:20] + ', '+ str(self.duration) + 'мин.'



# Модель Hall (Зал):
# Поля:
# name (название зала).
# capacity (вместимость зала).


class Hall(models.Model):
    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
    name = models.CharField(max_length=50,verbose_name = 'Название')
    capacity = models.IntegerField(verbose_name = 'Вместимость')

    def __str__(self):
        return self.name[0:10]

# Модель Session (Сеанс):
# Поля:
# movie (фильм).
# hall (зал).
# show_time (время показа).

class Session(models.Model):

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'


    movie = models.ForeignKey(Movie,on_delete=models.DO_NOTHING,verbose_name=Movie._meta.verbose_name)
    hall = models.ForeignKey(Hall,on_delete=models.DO_NOTHING,verbose_name=Hall._meta.verbose_name)
    show_time = models.TimeField(verbose_name='Продолжительность')
    price = models.IntegerField(verbose_name='Стоимость билета')

    def __str__(self):
        return str(self.hall) + ', '+ str(self.show_time) + ', '+ str(self.movie)

# Бронирование: информация о том, кто и на какой сеанс забронировал билеты.
# В админке подключать не будем. Так как для заполнения нужны свободные места в зале

class Ticket(models.Model):

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    session = models.ForeignKey(Session,on_delete=models.DO_NOTHING,verbose_name=Session._meta.verbose_name)
    purchase_date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=User._meta.verbose_name)

    def __str__(self):
        return f'зал: {self.session.hall} купил: {self.user.username}'
