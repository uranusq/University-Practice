from django.db import models
from django.utils import timezone


# Create your models here.

class Graph(models.Model):
    graph_name = models.CharField(max_length=200)
    x = models.TextField(default=0,max_length=100)
    y = models.TextField(default=0, max_length=100)
    file = models.FileField()
    date_published = models.DateTimeField(default=timezone.now)

class Formulas(models.Model):
    name = models.CharField(max_length=200)
    formula = models.TextField(default='x', max_length=100)





