from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('orders/', order_all, name='orders'),
    path('catalog/', catalog, name='catalog'),
    path('goods/<int:good>/<str:adik>',all_goods),
    path('add_good/',add_good, name='add_good'),
    path('all_users/',all_users, name='all_users'),
    path('shops/',shops, name='shops')
]
