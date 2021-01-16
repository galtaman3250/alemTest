from django.urls import path, reverse
from .views import *
from .views_serializers import *
from django.conf.urls import url
from alemsite import views_serializers
from rest_framework import routers


urlpatterns = [
    path('', index, name='home'),
    path('userRegister/', userRegister, name='userRegister'),
    path('userLogin/', userLogin, name='userLogin'),
    path('category/', category, name='category'),
    path('brand/', brand, name='brand'),
    path('color/', color, name='color'),
    path('favorites/<ai>/<name>/', favoritesView.as_view(), name='favorites'),
    path('gender/', gender, name='gender'),
    path('lastids/', lastids, name='lastids'),
    path('messages/', messageView.as_view(), name='messages'),
    path('order/<ai>/<name>/', orderView.as_view(), name='orders'),
    path('user/', user, name='user'),
    path('size/', size, name='size'),
    path('status/', status, name='status'),
    path('subcategory/', subcategory, name='subcategory'),
    path('cat/', catView.as_view(), name='cat'),
    path('sub/<int:category_id>/', subView.as_view(), name='sub'),
    path('product/<int:subcategory_id>/', proView.as_view(), name='product'),
    path('info/<int:pk>/', infoView.as_view(), name='infoProducts'),
    path('orderlist/', orderlistView, name='orderlist'),
    path('favlistt/', favlistView, name='favlist'),
    url(r'^brand-list/$', views_serializers.BrandList.as_view(), name=views_serializers.BrandList.name),
    url(r'^brand-list/(?P<pk>[0-9]+)$', views_serializers.BrandDetail.as_view(), name=views_serializers.BrandDetail.name),
    #url(r'^product-list/$', views_serializers.ProductList.as_view(), name=views_serializers.ProductList.name),
    url(r'^product-list/(?P<pk>[0-9]+)$', views_serializers.ProductDetail.as_view(), name=views_serializers.ProductDetail.name),
    url(r'^category-list/$', views_serializers.CategoryList.as_view(), name=views_serializers.CategoryList.name),
    url(r'^category-list/(?P<pk>[0-9]+)$', views_serializers.CategoryDetail.as_view(), name=views_serializers.CategoryDetail.name),
    url(r'^api/$', views_serializers.ApiRoot.as_view(), name=views_serializers.ApiRoot.name)


]







