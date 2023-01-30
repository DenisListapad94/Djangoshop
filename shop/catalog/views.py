from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.db import transaction

from .models import *
import json


def main(request):
    url = reverse(catalog)
    return render(request, 'main.html', {'url': url})


def catalog(request):
    url = reverse(main)
    clothes = Clothes.objects.all()
    return render(request, 'catalog.html', {"clothes": clothes, 'url': url})


def all_goods(request, good, adik):
    return HttpResponse(f"good number:{good} string {adik}")


def add_good(request):
    if request.method == 'POST':
        print(request.POST)
        # ar = Article.objects.create(article=request.POST['article'], serial_number='mc')
        Clothes.objects.create(name=request.POST['name'],
                               price=request.POST['price'],
                               size=request.POST['size'],
                               color=request.POST['color']
                              )
        redirect('/goods/main')
    return render(request, 'form_good_add.html')


def all_users(request):
    costumers = Costumers.objects.all()
    context = {
        "costumers": costumers
    }
    return render(request, 'all_users.html', context=context)


def shops(request):
    shops = Shop.objects.all()
    context = {
        "shops": shops
    }
    return render(request, 'shops.html', context=context)


def order_all(request):
    orders = Orders.objects.prefetch_related('clothes').all()
    context = {
        "orders": orders
    }
    return render(request, 'orders.html', context=context)

# @transaction.atomic
# def balance_view(request):
#     person = Costumers.objects.get(id=1)
#     person.balance -= 50
#     person.save()
#
#     raise ValueError
#     shop = Shop.objects.get(adress='pulcino')
#     shop.balance += 50
#     shop.save()
#     return HttpResponse('Потрачено')