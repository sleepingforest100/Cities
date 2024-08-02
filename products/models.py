from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    cities = models.ManyToManyField(City, related_name='products', blank=True)

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='photos')
    image = models.ImageField(upload_to='photos/', default='photos/default.jpg')

    def __str__(self):
        return f'{self.product} - {self.city}'
