from django.shortcuts import render

from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer,BookSerializer,ProductSerializer
from .models import Category,Book,Product

# Create your views here.

# class CategoryView(APIView):
#     def get(self,request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class BookView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    
#     def put(self,request,id=None):
#         return self.update(request,id)

# class ProductView(APIView):
#     def get(self,request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#Used generics here
class ListCategory(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class ListBook(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    

class ListProduct(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    