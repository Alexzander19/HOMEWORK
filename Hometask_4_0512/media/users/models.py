from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  # class Meta:
  #   verbose_name = 'Пользователь'
  #   verbose_name_plural = 'пользователи'
  # при настройке русского языка в settings они итак переходят на русский язык

  firstname = models.CharField(max_length=100,verbose_name='Имя доп.поле')
  lastname = models.CharField(max_length=100,verbose_name='Фамилия доп.поле')

  def __str__(self):
    return self.username