from rest_framework import serializers
from IM_service.models import *


class ProductSerializer(serializers.ModelSerializer):
        model = Products
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
        model = Suppliers
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
        model = Categories
        fields = "__all__"


class Sub_CategoryesSerializer(serializers.ModelSerializer):
        model = Sub_Categoryes
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
        model = Store
        fields = "__all__"

