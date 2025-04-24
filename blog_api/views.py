from django.shortcuts import render
from blog_api.serializer import *
from blog_api.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class Countryapi(APIView):
    def get(self,request,format=None):
        store = Countries.objects.all()
        serializer = Countriesserializer(store,many=True)
        return Response (serializer.data)
    
    def post(self,request,format=None):
        serializer = Countriesserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Countrycurd(APIView):
    def get_object(self,pk):
        try:
            return Countries.objects.get(pk=pk)
        except Countries.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        views = self.get_object(pk)
        serializer = Countriesserializer(views)
        return Response(serializer.data)
    
    def put(self,request,pk,format=True):
        views = self.get_object(pk)
        serializer = Countriesserializer(views,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        views = self.get_object(pk)
        views.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
class Userapi(APIView):
    def get(self,request,format=None):
        ss = User.objects.all()
        serializer = Userserializer(ss, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Userview(APIView):
    def get_data(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        views = self.get_data(pk)
        serializer = Userserializer(views)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        views = self.get_data(pk)
        serializer =Userserializer(views,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        h = self.get_data(pk)
        h.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
        
    

    
class Merchantapi(APIView):
    def get(self,request,format=None):
        ss = Merchants.objects.all()
        serializer = merchantsserializer(ss, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = merchantsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Merchantsview(APIView):
    def get_data(self,pk):
        try:
            return Merchants.objects.get(pk=pk)
        except Merchants.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        views = self.get_data(pk)
        serializer = merchantsserializer(views)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        views = self.get_data(pk)
        serializer =merchantsserializer(views,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        h = self.get_data(pk)
        h.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
       

class Orderapi(APIView):
    def get(self,request,format=None):
        ss = Order.objects.all()
        serializer = ordersserializer(ss, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = ordersserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Orderview(APIView):
    def get_data(self,pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        views = self.get_data(pk)
        serializer = ordersserializer(views)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        views = self.get_data(pk)
        serializer =ordersserializer(views,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        h = self.get_data(pk)
        h.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

class Order_item_api(APIView):
    def get(self,request,format=None):
        ss = order_item.objects.all()
        serializer = order_item_serializer(ss, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = order_item_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Orderview(APIView):
    def get_data(self,pk):
        try:
            return order_item.objects.get(pk=pk)
        except order_item.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        views = self.get_data(pk)
        serializer = order_item_serializer(views)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        views = self.get_data(pk)
        serializer =order_item_serializer(views,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        h = self.get_data(pk)
        h.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
class Products_api(APIView):
    def get(self,request,format=None):
        store = products.objects.all()
        serializer = products_serializer(store,many= True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = products_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class product_view(APIView):
    def get_object(self,pk):
        try:
            return products.objects.get(pk=pk)
        except products.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        views = self.get_object(pk)
        serializer = products_serializer(views)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        store = self.get_object(pk)
        serializer = products_serializer(store,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk,format=None):
        views = self.get_object(pk)
        views.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
            
        
        
        
        
    
        
    
    
    
        
    
    
    


    
        
        
        
            
        