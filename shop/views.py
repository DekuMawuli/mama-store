from django.shortcuts import render, redirect
from sendsms import api
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Product, Order


def home(request):
    products = Product.objects.all()
    ctx = {'products': products}
    if request.user.is_authenticated:
        order, _ = Order.objects.get_or_create(status=2, customer=request.user)
        ctx['order'] = order
    return render(request, "shopper/home.html", ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)


