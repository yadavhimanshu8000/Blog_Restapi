"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_api.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from blog_api import views

urlpatterns = [
    
    path('country/',Countryapi.as_view()),
    path('countryget/<int:pk>/', Countrycurd.as_view()),
    
    path('user/',Userapi.as_view()),
    path('userget/<int:pk>/',Userview.as_view()),
    
    path('merchants/',Merchantapi.as_view()),
    path('merchantsget/<int:pk>/',Merchantsview.as_view()),
    
    path('order/',Orderapi.as_view()),
    path('orderget/<int:pk>/',Orderview.as_view()),
    
    path('order_item/',Order_item_api.as_view()),
    path('order_item_get/<int:pk>/',Orderview.as_view()),
    
    path('production/',Products_api.as_view()),
    path('production_get/<int:pk>/',product_view.as_view()),  
]
urlpatterns = format_suffix_patterns(urlpatterns)
