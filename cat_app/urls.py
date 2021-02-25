from django.urls import path
from . import views
from rest_framework import routers 


app_name = 'prod_cat'



urlpatterns = [
    path('add_catprod/',views.add_catprod,name='add_catprod'),
    path('saveProd_cat/',views.saveProd_cat,name='saveProd_cat'),
    path('add_cat/',views.add_cat,name='add_cat'),
#    path('add_cat_save/',views.add_cat_saveView.as_view(),name='add_cat_save'),
    path('add_prod_savedata/',views.add_catsaveView.as_view(),name='add_prod_savedata'),
    path('catdetail/<str:name>/',views.CatDetailView.as_view(),name='catdetail'),
    path('prod_detail/<pk>/',views.prodDetailView.as_view(),name='prod_detail'),
    path('cat_Prodsearch/',views.cat_ProdsearchView,name='cat_Prodsearch'),
    path('cat_search/<pk>/',views.cat_searchView,name='cat_search'),
    path('upload_cat/',views.upload_cat,name='upload_cat'),
    path('upload_prod/',views.upload_prod,name='upload_prod'),
   ]
