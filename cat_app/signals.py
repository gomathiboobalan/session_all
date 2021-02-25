from django.db.models.signals import post_save, pre_delete
from order_app.models import OrderDb
from django.dispatch import receiver
from .models import Products

@receiver(post_save, sender=OrderDb)
def post_save_update_product(sender, instance, created, **kwargs):
    print('1post save')
    products=instance.prod_itm

    if instance.status == 3:
        print('post save')
        products.quantity = products.quantity - instance.itm_qty
        #print('prods')
        #prods.quantity = prods.quantity - instance.itm_qty
        products.save()
        print('post save1')