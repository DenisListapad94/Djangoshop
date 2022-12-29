from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import json


# goods = {
#     "jeans": 56.23,
#     "belt": 10.26,
#     "short": 9.12
# }


# menu = [{'url': "index", "field": 'Главная'},
#         {'url': "main", "field": 'все товары'},
# ]

def main(request):
    url = reverse(catalog)
    return render(request, 'main.html', {'url': url})


def catalog(request):
    url = reverse(main)
    with open("goods.json", 'r') as goods_json:
        goods = json.load(goods_json)
    return render(request, 'catalog.html', {"goods": goods, 'url': url})


def all_goods(request, good, adik):
    return HttpResponse(f"good number:{good} string {adik}")


def add_good(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'form_good_add.html')
