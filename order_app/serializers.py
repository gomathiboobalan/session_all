from rest_framework import serializers 
from .models import OrderDb
from cat_app.models import Category,Products
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer,TokenVerifySerializer
from rest_framework_simplejwt.tokens import RefreshToken,UntypedToken
from django.contrib.auth import get_user_model
#import stripe


User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDb
        fields= ['id','ord_user','prod_itm','itm_qty','total_amt','status']


class ProductSerializer(serializers.ModelSerializer):
    orders_for_prod = OrderSerializer(many=True,read_only=True)
    class Meta:
        model = Products
        fields=['id','name','price','orders_for_prod']

class CatSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields=['id','name','products']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        print('valid')
        print(attrs['username'])
        user = User.objects.get(username=attrs['username'])
        refresh = RefreshToken.for_user(user)
        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        }


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        data = {'access': str(refresh.access_token)}

        #if api_settings.ROTATE_REFRESH_TOKENS:
         #   if api_settings.BLACKLIST_AFTER_ROTATION:
          
          #      try:
                    # Attempt to blacklist the given refresh token
           #         refresh.blacklist()
            #    except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
             #       pass

           # refresh.set_jti()
            #refresh.set_exp()

        data['refresh'] = str(refresh)

        return data

class TokenVerifySerializer(TokenVerifySerializer):
    token = serializers.CharField()

    def validate(self, attrs):
        UntypedToken(attrs['token'])

        return {}



