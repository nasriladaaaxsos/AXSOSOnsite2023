from django.db import models

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=50)
    SecondName = models.CharField(max_length=50)
    Tele = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)




