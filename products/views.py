from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# Create your views here.
def index(request):
    f_product=Product.objects.order_by('priority')[:4]
    l_product=Product.objects.order_by('-id')[:4]
    context={
        'f_product':f_product,
        'l_product':l_product
    }
    return render(request,'index.html',context)

def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    productObj=Product.objects.order_by('priority')
    product_pag=Paginator(productObj,2)
    productObj=product_pag.get_page(page)
    context={'products':productObj}
    return render(request,'product.html',context)

def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={"product":product}
    return render(request,'product_detail.html',context)