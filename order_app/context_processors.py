from cat_app.models import Products,Category
from .models import OrderDb
from sess_main.models import CustomUser

def get_all_cat(request):
    if request.user.is_authenticated:
        
        categories = Category.catobj.all()

        return {'categories':categories}
    return {}


def no_cart_items(request):
    if request.user.is_authenticated:
        usr = CustomUser.objects.get(username=request.user)
        cart_count=OrderDb.objects.filter(ord_user=usr,status=5).count()
       # cart_count = order_data.count()
        return {'cart_count':cart_count}
    return {}


def get_user_pic(request):
    if request.user.is_authenticated:
        
        user = CustomUser.objects.get(username=request.user)

        return {'pic':user.profile_pic.url}
    return {}