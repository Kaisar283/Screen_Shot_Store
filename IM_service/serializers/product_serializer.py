from rest_framework import serializers
from IM_service.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"