from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products
from .serializers import ProductSerializer
from .serializers.product_serializer import Suppliers_productSerializer


class Supplier_ProductView(APIView):
    """
    Возвращает все продукты по  ID поставщика
    """

    def get(self, request, supple_id):
        products = Products.objects.filter(supplier_id=supple_id)
        serializer = Suppliers_productSerializer(products, many=True)
        return Response(serializer.data)


    # 16823

class Category_ProductsView(APIView):
    """
    Возвращает все продукты по  ID категорий
    """
    def get(self, request, cat_id):
        products = Products.objects.filter(category_id=cat_id)
        serializer = Suppliers_productSerializer(products, many=True)
        return Response(serializer.data)