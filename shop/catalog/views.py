from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
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
        return redirect('/goods/main')
    return render(request, 'form_good_add.html')
