from django.db import models
from cat_app.models import Category,Products
from sess_main.models import CustomUser
from django.db.models import Q

# Create your models here.

class OrderManager(models.Manager):
    def get_user_all_trackorders(self,uname):
        ord_u = CustomUser.objects.get(username=uname)
        return OrderDb.objects.filter(Q(ord_user=ord_u) & Q(status__in = ('3')))


    def get_user_all_order(self,uname):
        ord_u = CustomUser.objects.get(username=uname)
        return OrderDb.objects.filter(Q(ord_user=ord_u) & Q(status__in = ('1','2')))



    def get_user_cart_all(self,uname):
        ord_u = CustomUser.objects.get(username=uname)
        return OrderDb.objects.filter(Q(ord_user=ord_u) & Q(status = '5'))


class OrderDb(models.Model):
    id=models.AutoField(primary_key=True)
    ord_user=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='orderuser')
    prod_itm=models.ForeignKey(Products,on_delete=models.DO_NOTHING,related_name='orders_for_prod')
    itm_qty = models.PositiveIntegerField(default=1)
    total_amt=models.PositiveIntegerField(default=1)
    status_type=((1,"shipped"),(2,"delivered"),(3,"paid"),(5,'cart'))
    status=models.CharField(default=1,choices=status_type,max_length=10)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects= OrderManager()


   

    


    
