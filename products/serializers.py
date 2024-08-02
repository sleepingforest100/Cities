from rest_framework import serializers
from .models import Product, Photo

class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = ['image']

    def get_image(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url

class ProductSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'photos']

    def get_photos(self, obj):
        request = self.context.get('request')
        city_id = request.headers.get('CITY_ID')
        if city_id:
            city_photos = obj.photos.filter(city_id=city_id)
            if city_photos.exists():
                return PhotoSerializer(city_photos, many=True, context=self.context).data
        return PhotoSerializer(obj.photos.filter(city=None), many=True, context=self.context).data
