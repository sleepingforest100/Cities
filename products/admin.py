from django.contrib import admin
from .models import City, Product, Photo

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photos', 'get_city_names')

    def get_photos(self, obj):
        return obj.photos.count()
    get_photos.short_description = 'Number of Photos'

    def get_city_names(self, obj):
        return ', '.join(city.name for city in obj.cities.all())
    get_city_names.short_description = 'Cities'

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'city', 'get_image_url')

    def get_image_url(self, obj):
        return obj.image.url if obj.image else 'No Image'
    get_image_url.short_description = 'Image URL'
