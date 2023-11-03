from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    password = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.username
    

