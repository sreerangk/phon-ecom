from django.db import models
from django.contrib.auth.models import User
from django.forms import FilePathField

# Create your models here.
class user_tbl(models.Model):
    uname=models.CharField(max_length=200)
    uemail=models.EmailField()
    uage=models.IntegerField()
    
class udp(models.Model):
    userdt=models.OneToOneField(User,on_delete=models.CASCADE)
    dp=models.ImageField(upload_to='user_dp/',null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    addedon=models.DateTimeField(auto_now_add=True)
    updatedon=models.DateTimeField(auto_now=True)
    contact_no=models.IntegerField(null=True,blank=True)

Gender_choices =(
    ('mobile','m'),
    ('hedset','h')
)

class Products(models.Model):
    productname = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category= models.CharField(choices=Gender_choices,max_length=6)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now=True,null=True)
    updated_on=models.DateTimeField(auto_now=True,null=True) 