
from django.contrib import admin
from .models import City, Product, Photo

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photos', 'get_city_name')

    def get_photos(self, obj):
        return obj.photos.count()
    get_photos.short_description = 'Number of Photos'

    def get_city_name(self, obj):
        return ', '.join(city.name for city in obj.cities.all())
    get_city_name.short_description = 'Cities'
