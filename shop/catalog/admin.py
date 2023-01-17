from django.contrib import admin
from .models import *


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size')
    list_display_links = ('name',)
    search_fields = ('name', 'price')
    list_editable = ('price', 'size')
    list_filter = ('name', 'price', 'size')
    # list_per_page = 3  # пагинация


admin.site.register(Clothes, ClothesAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'adress')
    list_display_links = ('name', 'surname')


admin.site.register(Users, UsersAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article', 'serial_number')
    list_display_links = ('article',)


admin.site.register(Article, ArticleAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user','shop','order_date')
    list_display_links = ('user',)


admin.site.register(Orders, OrdersAdmin)

class ShopAdmin(admin.ModelAdmin):
    list_display = ('main_manager', 'phone')
    list_display_links = ('main_manager',)


admin.site.register(Shop, ShopAdmin)