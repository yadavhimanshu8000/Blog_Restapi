from rest_framework import serializers
from .models import Countries, User, Merchants, Order, order_item, products


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['name', 'continent_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'gender', 'date_of_birth', 'country_code']


class MerchantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchants
        fields = [ 'merchant_name', 'admin_id', 'country_code']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user_id', 'status']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_item
        fields = ['order_id', 'product_id', 'quantity']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['merchants_id', 'name', 'price']
