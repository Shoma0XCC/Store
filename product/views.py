from django.shortcuts import render, HttpResponseRedirect
from product.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    context = { 'title': 'Test title',}
    return render(request, 'product/index.html', context)


def product(request, category_id=None, page=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)

    context = {'title': 'Store - Каталог',
               'categories': ProductCategory.objects.all(),
               'products': products_paginator,}
    return render(request, "product/product.html", context)

@login_required
def basket_add(request, product_id):
    products = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=products)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=products, quantity=1)

    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

