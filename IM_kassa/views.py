from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from IM_service.models import Products
from .serializers import Product_kassaSerializer, SaleSerializer
from .models import Sales_History


class Product_ByIDView(APIView):

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('prod_id')
        product = Products.objects.get(product_id=product_id)
        serializer = Product_kassaSerializer(product)
        return Response(serializer.data)


class Product_ByBarcodeView(APIView):

    def get(self, request, *args, **kwargs):
        barcode = kwargs.get('barcode')
        product = Products.objects.get(barcode=barcode)
        serializer = Product_kassaSerializer(product)
        return Response(serializer.data)


class KassaSaleAPICreate(generics.CreateAPIView):
    queryset = Sales_History.objects.all()
    serializer_class = SaleSerializer





