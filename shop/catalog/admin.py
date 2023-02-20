from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
class ShopInline(admin.TabularInline):
    model = Shop

class OrderInline(admin.StackedInline):
    model = Orders
    extra = 1

@admin.action(description='available clothes')
def make_available(modeladmin, request, queryset):
    queryset.update(status='a')
@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    # fields = ['name', 'price', 'size', 'color','description','cheap_clothes']
    # exclude = ('article',)

    list_display = ('name', 'price', 'size', 'color','strike_clothes','cheap_clothes','status')
    list_display_links = ('name',)
    list_filter = ('name', 'price')
    search_fields = ('name', 'color')
    readonly_fields = ('size','cheap_clothes')
    list_per_page = 30
    ordering = ('name', 'price')
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (('name', 'price'), 'size', 'color','cheap_clothes','status')
        }),
        ('Advanced options', {
            # 'classes': ('collapse',),
            'fields': ('description', 'category'),
        }),
    )
    inlines = [
        ShopInline,
        OrderInline
    ]
    @admin.display(description='category clothes')
    def cheap_clothes(self,object):
        if object.price:
            return 'cheap' if object.price < 100 else 'expensive'
        else:
            return 'sold'

    def strike_clothes(self,object):
        return mark_safe(f"<s>{object.name}</s>") if not object.price else object.name

    @admin.action(description='sold clothes')
    def make_sold(self, request, queryset):
        queryset.update(status='s')

    actions = [make_available, make_sold]

#
# admin.site.register(Clothes, ClothesAdmin)


class CostumersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'adress', 'balance')
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
    list_display = ('adress', 'phone', 'balance','get_html_photo')
    list_display_links = ('adress',)
    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f"<img width=50 src={object.photo.url}/>")

    get_html_photo.short_description = 'фото'
admin.site.register(Shop, ShopAdmin)
