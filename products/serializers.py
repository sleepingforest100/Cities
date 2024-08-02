from rest_framework import serializers
from .models import Product, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'photos']

    def get_photos(self, obj):
        request = self.context.get('request')
        city_id = request.headers.get('City-ID')

        if city_id:
            city_photos = obj.photos.filter(city_id=city_id)
            if city_photos.exists():
                return PhotoSerializer(city_photos, many=True).data

        common_photos = obj.photos.filter(city__isnull=True)
        return PhotoSerializer(common_photos, many=True).data
