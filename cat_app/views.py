from django.shortcuts import render
from .forms import ProdForm,CatForm
from .models import Category,Products
from django.urls import reverse_lazy
from django.contrib import messages
from tablib import Dataset
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,UpdateView,DeleteView,DetailView
                                )
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from sess_main.decorators import merchant_required, customer_required
from django.urls import reverse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

@login_required
@merchant_required
def add_catprod(request):
    print('prod add')
    form = ProdForm
    return render(request,'products/addprod.html',{'form':form})


@login_required
@merchant_required
def saveProd_cat(request):
    if request.method != "POST":
        form = ProdForm()
        return render(request,'products/addprod.html',{'form':form})
    elif request.method == "POST":
        print('post')
       # form = ProdForm(request.POST)
        try:
           # if form.is_valid():
            print('valid')
            name = request.POST.get('name')
            short_des = request.POST.get('short_des')
            long_des = request.POST.get('long_des')
            price = request.POST.get('price')
            quantity = request.POST.get('quantity')
            print('name')
            cat_value=request.POST.get('catprod')
            print(cat_value)
            cat_item = Category.catobj.get(name=cat_value)
            print(cat_item)
            print('sss')
            prod_img = request.FILES.get('prod_img')
            print('query')
            if cat_item:
                print('query inside')
                product_model = Products(name=name,prodcat=cat_item,short_des=short_des,long_des=long_des,price=price,quantity=quantity)
                print('before saved')
                product_model.prod_img=prod_img
                print('savedafter')
                product_model.save()
                print('saved')
                messages.success(request,"saved record")
                form = ProdForm()
                return HttpResponseRedirect(reverse("prod_cat:add_catprod"))
            else:
                print('save error')
                form = ProdForm()
                #form.fields['name'].initial=form.cleaned_data['catprod']
                return HttpResponseRedirect(reverse("prod_cat:add_catprod"))
        except Exception as e:
            print(type(e))
            messages.error(request,"category not available error record")
            form = ProdForm(request.POST)
            return HttpResponseRedirect(reverse("prod_cat:add_catprod"))
        form = ProdForm()
        return HttpResponseRedirect(reverse("prod_cat:add_catprod"))


@login_required
@merchant_required
def add_cat(request):
    print('cat_app')
    form = CatForm
    return render(request,'category/addcat.html',{'form':form})


class add_catsaveView(CreateView):
    print('cat_app save')
    def get(self, request, *args, **kwargs):
        context = {'form': CatForm()}
        return render(request, 'category/addcat.html', context)

    def post(self, request, *args, **kwargs):
        form = CatForm(request.POST)
        if form.is_valid():
            cat = form.save()
            cat.save()
           # return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
            return HttpResponseRedirect(reverse_lazy('prod_cat:add_cat'))
        return render(request, 'category/addcat.html', {'form': form})
    

class CatDetailView(DetailView):
    model = Category


class prodDetailView(DetailView):
    model = Products
    template_name='products/proddetail.html'
    context_name = 'product'


def cat_searchView(request,pk):
    print('search')
    cat_model = Category.catobj.get(id=pk)
   
    try:
        if cat_model:
            print(cat_model)
            prods_model = Products.objects.filter(prodcat=cat_model)
            print(prods_model)
            products_data=[]
    
            for prod in prods_model:
                
                prod_data={'name' : prod.name,
            'price':prod.price,
            'id':prod.id,
            'quantity':prod.quantity,
            'img':prod.prod_img.url
                    }
                products_data.append(prod_data)
            page=request.GET.get('page',1)
            paginator=Paginator(products_data,6)
            try:
                products_list=paginator.page(page)
            except PageNotAnInteger:
                products_list=paginator.page(1)
            except EmptyPage:
                products_list=paginator.page(paginator,num_pages)
            #context=products_list)
            return render(request,'registration/index.html',{'products':products_list})
            #return HttpResponseRedirect('/sess/index/',kwargs={'products':products_list})
    except Exception as e:
        print(type(e))
        return render(request,'registration/index.html',{})


def cat_ProdsearchView(request):
    if request.method!= "POST":
        name=request.GET.get('search')
        cat_model = Category.catobj.get(name=name)
        try:
            if cat_model:
                prods_model = Products.objects.filter(prodcat=cat_model)
            else:   
                prods_model = Products.objects.filter(name=name)
            
            products_data=[]
    
            for prod in prods_model:
                
                prod_data={'name' : prod.name,
                'price':prod.price,
                'id':prod.id,
                'quantity':prod.quantity,
                'img':prod.prod_img.url
                }
                products_data.append(prod_data)
            page=request.GET.get('page',1)
            paginator=Paginator(products_data,6)
            try:
                products_list=paginator.page(page)
                return render(request,'registration/index.html',{'products':products_list})
            except PageNotAnInteger:
                products_list=paginator.page(1)
                return render(request,'registration/index.html',{'products':products_list})
            except EmptyPage:
                products_list=paginator.page(paginator,num_pages)
                return render(request,'registration/index.html',{'products':products_list})
            print('many')
            print(products_list)
            return render(request,'registration/index.html',{'products':products_list})
                #return HttpResponseRedirect('/sess/index/',kwargs={'products':products_list})
        except Exception as e:
            print(type(e))
            return HttpResponse("error while processing records")
            #return HttpResponseRedirect('/sess/index/',kwargs={'products':products_list})
    
    return render(request,'registration/index.html',{})


def upload_cat(request):
    if request.method == 'POST':
        cat_r = CategoryResource()
        dataset = Dataset()
        new_cat = request.Files['myfile']
        recs = dataset.load(new_cat.read(),format='xlsx')
        for rec in recs:
            value=Category(data[0],data[1],data[2],data[3])
            value.save()
            print('rec saved')
    else:
        print('upload')
    
    return render(request,'category/catupload.html',{}) 


def upload_prod(request):
    if request.method == 'POST':
        prd_r = ProductsResource()
        dataset = Dataset()
        new_prd = request.Files['myfile']
        recs = dataset.load(new_prd.read(),format='xlsx')
        for rec in recs:
            value=Products(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
            value.save()
            print('rec saved')

    else:
        print('upload')
        return render(request,'products/produpload.html',{}) 



