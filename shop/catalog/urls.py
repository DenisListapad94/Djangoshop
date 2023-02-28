from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('main/', main, name='main'),
    path('orders/', order_all, name='orders'),
    path('catalog/', catalog, name='catalog'),
    path('goods/<int:good>/<str:adik>', all_goods),
    path('add_good/', add_good, name='add_good'),
    path('all_users/', all_users, name='all_users'),
    path('shops/', shops, name='shops'),
    path('feedback_form/', feedback_form, name='feedback_form'),
    path('add_shop_form/', add_shop_form, name='add_shop_form'),
    path('mine/', MyView.as_view(), name='my-view'),
    path('create_shop/', ShopCreateView.as_view(), name='create_shop'),
    path('api/clothes', ClothesListApiView.as_view(), name="clothes_api"),
    re_path('api/clothes/(?P<pk>[\d-]+)', cache_page(60,cache='default')(ClothesApiDetailView.as_view()), name='show_detail_api'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/',logout_user,name='logout')
    # path('balance_view/',balance_view, name='balance_view')
]
