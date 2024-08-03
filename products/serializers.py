from rest_framework import serializers
from .models import Product, Photo, City

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image', 'city']

class ProductSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    cities = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'photos', 'cities']

    def get_photos(self, obj):
        request = self.context.get('request')
        city_id = request.headers.get('City-ID')

        if city_id:
            city_photos = obj.photos.filter(city_id=city_id)
            if city_photos.exists():
                return PhotoSerializer(city_photos, many=True).data

        common_photos = obj.photos.filter(city__isnull=True)
        return PhotoSerializer(common_photos, many=True).data

    def get_cities(self, obj):
        cities = City.objects.filter(photos__product=obj).distinct()
        return [city.name for city in cities]
