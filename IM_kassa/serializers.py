from rest_framework import serializers
from IM_service.models import Products
from .models import Sales_History

class Product_kassaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_id', 'barcode', 'product_name', 'sale_price')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales_History
        fields = '__all__'