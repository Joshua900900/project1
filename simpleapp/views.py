from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'simpleapp/product_list.html', {'products': products})

def welcome_page(request):
    return render(request, 'simpleapp/welcome_page.html')
