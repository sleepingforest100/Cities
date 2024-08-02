# products/models.py
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    cities = models.ManyToManyField(City, blank=True, related_name='products')

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    product = models.ForeignKey(Product, related_name='photos', on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
