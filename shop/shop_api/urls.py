from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('clothes_all/', ClothesApiView.as_view(), name='api_all_clothes'),
    path('clothes/', ClothesApiView.as_view(), name='clothes_api'),
    re_path('clothes/(?P<pk>[\d-]+)', ClotheApiView.as_view(), name='clothes_api'),

]