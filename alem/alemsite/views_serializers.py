from rest_framework import generics
from .models import Brand, Products, Category
from .serializers import BrandSerializer, ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    name = 'brand-list'


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    name = 'brand-detail'


#class ProductList(generics.ListCreateAPIView):
    #queryset = Products.objects.all()
    #serializer_class = ProductSerializer
    #name = 'product-list'

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'alem'

    def get(self, request, *args, **kwargs):
        return Response({
            'brands': reverse(BrandList.name, request=request),
            #'products': reverse(ProductList.name, request=request),
            'categories': reverse(CategoryList.name, request=request),

            })
