from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClothesSerializer,ClothesModelSerializer

from catalog.models import Clothes


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