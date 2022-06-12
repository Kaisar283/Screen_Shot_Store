from rest_framework import serializers
from IM_service.models import *


class ProductSerializer(serializers.ModelSerializer):
        class Meta:
                model = Products
                fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
        class Meta:
                model = Suppliers
                fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
        class Meta:
                model = Categories
                fields = "__all__"


class Sub_CategoryesSerializer(serializers.ModelSerializer):
        class Meta:
                model = Sub_Categoryes
                fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
        class Meta:
                model = Store
                fields = "__all__"


class Suppliers_productSerializer(serializers.ModelSerializer):
        class Meta:
                model = Products
                exclude = ('store_id', 'unit_price', 'sale_price')

