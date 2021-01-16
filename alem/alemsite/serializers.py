from rest_framework import serializers
from .models import Brand, Products, Category


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Brand
        fields = ('url', 'name', 'products', )


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Products
        fields = ('name',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Category
        fields = ('url', 'ai', 'name', 'products')
