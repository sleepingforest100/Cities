from django.urls import reverse
from rest_framework.test import APITestCase
from .models import City, Product

class ProductTests(APITestCase):
    def setUp(self):
        self.city = City.objects.create(name="Test City")
        self.product = Product.objects.create(name="Test Product", photo="http://example.com/photo.jpg", city=self.city)
        self.url = reverse('product-list')

    def test_get_products_with_city_id(self):
        response = self.client.get(self.url, HTTP_CITY_ID=self.city.id)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Product")

    def test_get_products_without_city_id(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Product")
