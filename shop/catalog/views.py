from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.views import View

from django.db import transaction
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView, BaseListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin

from .models import *
from .forms import *
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

@permission_required('catalog.add_shop',login_url='/admin/login/')
def add_shop_form(request):
    context = {}
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save()
            return redirect('main')
        context['form'] = ShopForm(request.POST)
    else:
        context['form'] = ShopForm()
    return render(request, 'add_shop_form.html', context=context)


def all_users(request):
    costumers = Costumers.objects.all()
    context = {
        "costumers": costumers
    }
    return render(request, 'all_users.html', context=context)


def feedback_form(request):
    context = {}
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(**form.cleaned_data)
            return redirect('main')
        context['form'] = FeedbackForm(request.POST)
    else:
        context['form'] = FeedbackForm()
    return render(request, 'feedback_form.html', context=context)

@permission_required('catalog.view_shop',login_url='/admin/login/')
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

# @permission_required('catalog.view_shop',login_url='/admin/login')
class MyView(ListView,PermissionRequiredMixin):
    permission_required = 'catalog.view_shop'
    template_name = "home.html"
    model = Shop
    context_object_name = "shops"
    # def get_queryset(self):
    #     return Shop.objects.all()[:3]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['shops'] = Shop
    #     return context


class ShopCreateView(CreateView):
    template_name = "create_shop.html"
    model = Shop
    fields = ['adress', 'phone', 'balance']
    success_url = reverse_lazy("my-view")


class SerializersClothesMixin():
    def serialize(self, clothes):
        return {'id': clothes.id, "name": clothes.name}


class ClothesListApiView(BaseListView, SerializersClothesMixin):
    model = Clothes
    context_object_name = 'clothes'

    def render_to_response(self, context):
        data = [self.serialize(clothes) for clothes in context['clothes'][:20]]
        # data = [{'id': clothes.id, "name": clothes.name} for clothes in context['clothes'][:20]]
        body = json.dumps(data)
        return HttpResponse(body, content_type='application/json', status=200)


class ClothesApiDetailView(DetailView, SerializersClothesMixin):
    model = Clothes
    context_object_name = 'clothes'

    def render_to_response(self, context):
        # data = {'id': context['clothes'].id, "name": context['clothes'].name}
        data = self.serialize(context['clothes'])
        body = json.dumps(data)
        return HttpResponse(body, content_type='application/json', status=200)

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
