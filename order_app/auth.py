from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token 
from rest_framework.response import Response
#from django.contrib.auth.models import User
#from sess_main.models import CustomUser

from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        user_n = request.data['username']
        
        #serializer= self.serializer_class(data=request.data)
        try:
            print('av')
            user = User.objects.get(username=user_n)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key,'user_id':user.pk,'email':user.email})
        except Exception as e:
            print(type(e))
            return Response({'eorror':'error'})
        return Response({'eorror':'error'})