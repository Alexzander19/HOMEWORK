from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    price = models.IntegerField()
    date_create = models.DateField(auto_now_add=True)
    pict = models.ImageField(upload_to='static/images')

    def __str__(self):
        return f'{self.name}: {self.about[0:20]}... стоимость: {self.price} руб.'

#  Обратная связь. Возможность оставить запрос на конкретную услугу
class Interested(models.Model):
    service = models.ForeignKey(Services,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    request = models.TextField()
    date_time_create = models.DateTimeField(auto_now_add=True)