from django.db import models


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,unique=True)
    short_des=models.CharField(max_length=50)
    long_des=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    catobj = models.Manager()


class Products(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    prodcat=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    short_des=models.CharField(max_length=50)
    long_des=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    prod_img=models.ImageField(upload_to='uploads/products/', null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    


#class Proditem(Products):
 #   class Meta:
  #      Proxy=True
    