from django.contrib import admin
from .models import *


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'dress_style')
    list_display_links = ('name','dress_style')
    search_fields = ('name', 'price')
    list_editable = ('price', 'size')
    list_filter = ('name', 'price', 'size')
    # list_per_page = 3  # пагинация


admin.site.register(Clothes, ClothesAdmin)


class DressStyleAdmin(admin.ModelAdmin):
    list_display = ('title_style',)
    list_display_links = ('title_style',)


admin.site.register(Dress_style, DressStyleAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article',)
    list_display_links = ('article',)


admin.site.register(Article, ArticleAdmin)
