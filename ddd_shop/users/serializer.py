import json

from rest_framework import serializers
from .models import Product, Store, Store


class ShowProductSerializer(serializers.ModelSerializer):
   # product_skus = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ("name", "product_id", "category_id")
   
        fields = '__all__'
        depth = 1


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "category_id", "product_id")
        fields = '__all__'


class CreateStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("name", "store_id", "owner_id")
        fields = '__all__'
