from cat_app.models import Category,Products
from django.forms import ModelForm
from django import forms
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.forms import inlineformset_factory

class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','short_des','long_des')


class ProdForm(forms.ModelForm):
    catprod = forms.CharField(max_length=50)
    class Meta:
        model = Products
        fields = ('name','short_des','long_des','price','quantity','prod_img')


