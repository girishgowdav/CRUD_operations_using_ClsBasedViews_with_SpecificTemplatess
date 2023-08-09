from django.db import models

# Create your models here.
from django.urls import reverse

class School(models.Model):
    Scname=models.CharField(max_length=100)
    Schead=models.CharField(max_length=100)
    Scloc=models.CharField(max_length=100)

    def __str__(self):
        return self.Scname

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.CharField(max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='student')

    def __str__(self):
        return self.Sname