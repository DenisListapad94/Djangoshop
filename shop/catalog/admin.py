from django.contrib import admin
from .models import *


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size','article')
    list_display_links = ('name',)
    search_fields = ('name', 'price')
    list_editable = ('price', 'size')
    list_filter = ('name', 'price', 'size')
    # list_per_page = 3  # пагинация


admin.site.register(Clothes, ClothesAdmin)


class CostumersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'adress','balance')
    list_display_links = ('name',)
    ordering = ('id',)


admin.site.register(Costumers, CostumersAdmin)


class ManagersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'adress')
    list_display_links = ('name', 'surname')


admin.site.register(Managers, ManagersAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article', 'serial_number')
    list_display_links = ('article',)


admin.site.register(Article, ArticleAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_date',)
    list_display_links = ('order_date',)


admin.site.register(Orders, OrdersAdmin)


class ShopAdmin(admin.ModelAdmin):
    list_display = ('adress', 'phone','balance')
    list_display_links = ('adress',)


admin.site.register(Shop, ShopAdmin)
