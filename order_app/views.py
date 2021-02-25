from django.shortcuts import render
from .models import OrderDb
from sess_main.models import CustomUser
from cat_app.models import Category,Products
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (CreateView,UpdateView,DeleteView,ListView
                                )
from rest_framework import viewsets 
from .serializers import OrderSerializer,ProductSerializer,CatSerializer,MyTokenObtainPairSerializer,MyTokenRefreshSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# Create your views here.
def add_to_cart(request,id):
    cust_user=CustomUser.objects.get(username=request.session.get('name'))
    #prod_mod = Products.objects.filter(name__in='makeups')
    prod_mod = Products.objects.get(id=id)
    
    cust_prod , created=OrderDb.objects.get_or_create(ord_user=cust_user,prod_itm=prod_mod,status = '5')
   
    #cust_prod = OrderDb.objects.get_user_all_ordersprod(request.session.get('name'),'makeups')
    if not created:
        
        cust_prod.itm_qty = cust_prod.itm_qty + 1
        cust_prod.total_amt = cust_prod.itm_qty * 20
       
        cust_prod.save()
       
        print(prod_mod.name)
       # return render(request,'registration/index.html',{'products':prod_mod})
       
    else:
        
       # cust_prod_model = OrderDb(ord_user=cust_user,prod_itm=prod_mod)
        cust_prod.itm_qty =  1
        cust_prod.total_amt = 40 * cust_prod.itm_qty
        cust_prod.status = 5
        cust_prod.save()
        
        print(prod_mod.name)
        print('created')
    return HttpResponseRedirect(reverse("sess:index"))
      
        # return render(request,'registration/index.html',{'products':prod_mod})
    

class view_cart(ListView):
    model=OrderDb
    template_name='orders/cart.html' 
    #context_object_name = 'qs'

    #def get_queryset(self):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subtotal = 0
        qs = OrderDb.objects.get_user_cart_all(self.request.user)
        for q in qs:
            subtotal = q.total_amt + subtotal
        tax = subtotal * 0.05
        total = subtotal + tax
        context["qs"]=qs
        context["tax"]=tax
        context["total"]=total
        context["subtotal"]=subtotal
        return context 

def add_quantity(request,id):
    ord = OrderDb.objects.get(id=id)
    
    ord.itm_qty = ord.itm_qty + 1
    ord.total_amt = ord.itm_qty * ord.prod_itm.price
    ord.save()
    return HttpResponseRedirect(reverse('order_prod:view_cart'))

def del_quantity(request,id):
    ord = OrderDb.objects.get(id=id)
    
    ord.itm_qty = ord.itm_qty - 1
    ord.total_amt = ord.itm_qty * ord.prod_itm.price
    ord.save()
    return HttpResponseRedirect(reverse('order_prod:view_cart'))


def del_cart_item(request,id):
    ord = OrderDb.objects.get(id=id)
    ord.delete()
    return HttpResponseRedirect(reverse('order_prod:view_cart'))


def make_payment(request):
    ords = OrderDb.objects.get_user_cart_all(request.user)
    for ord in ords:
        ord.status = 3
        ord.save()
    return HttpResponseRedirect(reverse('order_prod:view_cart'))


def track_orders(request):
    trk_ords = OrderDb.objects.get_user_all_trackorders(request.user)
    return render(request,'orders/trackorders.html',{'trk_ords':trk_ords})


class orderViewset(viewsets.ModelViewSet):
    queryset=OrderDb.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['status']
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class prodViewset(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_fields = ['name']
    ordering_fields = ['id']
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class catViewset(viewsets.ModelViewSet):
    queryset=Category.catobj.all()
    serializer_class = CatSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
   

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    serializer_class = MyTokenRefreshSerializer