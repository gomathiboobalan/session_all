from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
from order_app.auth import CustomAuthToken
#from rest_framework.authtoken.views import obtain_auth_token
from .views import MyTokenObtainPairView, MyTokenRefreshView

app_name = 'order_prod'

router = DefaultRouter() 
router.register('ord', views.orderViewset,basename='ords')
router.register('prd', views.prodViewset,basename='prods')
router.register('cat', views.catViewset,basename='cats')

urlpatterns = [
    path('', include(router.urls)), 
    path('add_to_cart/<id>/',views.add_to_cart,name='add_to_cart'),
    path('view_cart/',views.view_cart.as_view(),name='view_cart'),
    path('add_quantity/<id>/',views.add_quantity,name='add_quantity'),
    path('del_quantity/<id>/',views.del_quantity,name='del_quantity'),
    path('del_cart_item/<id>/',views.del_cart_item,name='del_cart_item'),
    path('make_payment/',views.make_payment,name='make_payment'),
    path('track_orders/',views.track_orders,name='track_orders'),
    path('auth/',include('rest_framework.urls')),
  #  path('gettoken/',CustomAuthToken.as_view()),
    path('getjwttoken/',MyTokenObtainPairView.as_view()),
    path('refreshjwttoken/',MyTokenRefreshView.as_view()),
 #   path('gettoken/',obtain_auth_token)
]