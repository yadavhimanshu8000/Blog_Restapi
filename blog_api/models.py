from django.db import models

# Create your models here.

class Countries(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    continent_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,unique=True)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    country_code = models.ForeignKey(Countries,on_delete=models.CASCADE,related_name='country_code')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    
class Merchants(models.Model):
    id = models.AutoField(primary_key=True)
    merchant_name = models.CharField(max_length=100)
    admin_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='admin')
    country_code = models.ForeignKey(Countries,on_delete=models.CASCADE,related_name='countrycode')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.merchant_name
    
       
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_id')
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
class order_item(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order')
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.quantity
    
class products(models.Model):
    id = models.AutoField(primary_key=True)
    merchants_id = models.ForeignKey(Merchants,on_delete=models.CASCADE,related_name='merchant')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    status = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
    
