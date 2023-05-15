from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    in_draft = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)