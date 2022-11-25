from django.db import models

# Create your models here.

class myfrd(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DOB = models.DateField(max_length=8)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=10)


