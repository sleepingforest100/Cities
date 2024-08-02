from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'photo', 'photos']

    def get_photos(self, obj):
        request = self.context.get('request')
        city_id = request.headers.get('City-ID') if request else None
        if city_id:
            pass
        return obj.photo
