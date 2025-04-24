from rest_framework import serializers
from blog_api.models import *

class Countriesserializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'
        
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class merchantsserializer(serializers.ModelSerializer):
    class Meta:
        model = Merchants
        fields = '__all__'
        
class ordersserializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class order_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = order_item
        fields = '__all__'
        
class products_serializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = "__all__"
        
        
        
        