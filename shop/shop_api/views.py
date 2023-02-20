from django.shortcuts import render
from rest_framework import status, generics, views
from rest_framework.parsers import JSONParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

from catalog.models import Clothes,Shop


# class ClothesApiView(APIView):
#     def get(self, request, format=None):
#         clothes = Clothes.objects.all()
#         serializer = ClothesSerializer(clothes, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ClothesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClothesApiView(generics.ListCreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesModelSerializer

class ClotheApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesModelSerializer

class ShopApiView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer

class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]
    def put(self, request, pk, format=None):
        file_obj = request.data['file']
        obj = Shop.objects.get(pk=pk)
        obj.photo = file_obj
        obj.save()
        return Response(status=204)