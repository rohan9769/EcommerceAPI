from rest_framework import serializers

from .models import Category,Book,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','category','isbn','pages','price','stock','description','imageUrl','status','date_created']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_tag','name','category','price','stock','imageUrl','status','date_created']
