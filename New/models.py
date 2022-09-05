from unicodedata import name
from xml.etree.ElementTree import Comment
from django.db import models

# Create your models here.
class Contactus(models.Model):
    name =models.CharField(max_length=50)
    email=models.TextField(max_length=50)
    phone=models.CharField(max_length=12)
    Comment=models.TextField(max_length=100)
    date = models.DateField()
