from rest_framework import serializers
from product.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(required=False, source='user.email')


    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(required=False, source='user.email')


    class Meta:
        model = Category
        fields = '__all__'
