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
    description = models.TextField()

    def __str__(self):
        return self.title[0:20] +', ' + self.genre[0:20] + ', '+ str(self.duration) + 'мин.'



# Модель Hall (Зал):
# Поля:
# name (название зала).
# capacity (вместимость зала).


class Hall(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name[0:10]

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

    def __str__(self):
        return str(self.hall) + ', '+ str(self.show_time) + ', '+ str(self.movie)

# Бронирование: информация о том, кто и на какой сеанс забронировал билеты.
# В админке подключать не будем. Так как для заполнения нужны свободные места в зале

class Ticket(models.Model):
    session = models.ForeignKey(Session,on_delete=models.DO_NOTHING)
    purchase_date_time = models.DateTimeField(auto_now_add=True)
