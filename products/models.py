from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/481px-Cat03.jpg')  
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)  
