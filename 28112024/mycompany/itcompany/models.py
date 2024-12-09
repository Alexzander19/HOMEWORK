from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    price = models.IntegerField()
    date_create = models.DateField(auto_now_add=True)
    pict = models.ImageField(upload_to='static/images')
