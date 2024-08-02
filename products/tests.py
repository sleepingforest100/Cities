from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import City, Product, Photo

class ProductTests(APITestCase):
    def setUp(self):
        self.city = City.objects.create(name='Oskemen')
        self.product = Product.objects.create(name='TestProduct')
        self.common_photo = Photo.objects.create(image='https://w0.peakpx.com/wallpaper/528/988/HD-wallpaper-piece-of-cake-cake-food-thumbnail.jpg', product=self.product)
        self.city_photo = Photo.objects.create(image='https://wallpapers.com/images/featured/cake-pictures-806wm5ug2sx0o5ld.jpg', product=self.product, city=self.city)
        self.url = reverse('product-list')

    def test_get_products_without_city_id(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]['photos']), 1)
        self.assertEqual(
            response.data[0]['photos'][0]['image'],
            'http://testserver/media/https%3A/w0.peakpx.com/wallpaper/528/988/HD-wallpaper-piece-of-cake-cake-food-thumbnail.jpg'
        )

    def test_get_products_with_city_id(self):
        response = self.client.get(self.url, HTTP_CITY_ID=self.city.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]['photos']), 1)
        self.assertEqual(
            response.data[0]['photos'][0]['image'],
            'http://testserver/media/https%3A/wallpapers.com/images/featured/cake-pictures-806wm5ug2sx0o5ld.jpg'
        )
