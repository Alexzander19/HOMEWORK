from django.db import models

# Create your models here.


# Модель Movie (Фильм):
# Поля:
# title (название фильма).
# duration (длительность фильма в минутах).
# genre (жанр фильма).
# release_date (дата выхода фильма).


class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)
    release_date = models.DateField()



# Модель Hall (Зал):
# Поля:
# name (название зала).
# capacity (вместимость зала).


class Hall(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

# Модель Session (Сеанс):
# Поля:
# movie (фильм).
# hall (зал).
# show_time (время показа).

class Session(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.DO_NOTHING)
    hall = models.ForeignKey(Hall,on_delete=models.DO_NOTHING)
    show_time = models.TimeField()
    price = models.IntegerField()
