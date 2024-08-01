from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse

class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

def home(request):
    return HttpResponse("Welcome to the Product API!")