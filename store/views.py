from django.shortcuts import render, get_object_or_404
from . models import Products


def index(request):
    all_products = Products.objects.all()
    return render(request, 'store/index.html', {'all_products': all_products})


def detail(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    return render(request, 'store/detail.html', {'product': product})


def purchase(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    return render(request, 'store/purchase.html', {'product': product})

def cart(request, product_id):   #attach to purchase
    product = get_object_or_404(Products, pk=product_id)