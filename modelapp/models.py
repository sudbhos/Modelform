from django.db import models

# Create your models here.

class studentinfo(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField()
    std=models.IntegerField()