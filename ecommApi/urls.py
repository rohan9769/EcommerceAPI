from django.urls import path,include
from .views import ListCategory,DetailCategory,ListBook,DetailBook,ListProduct,DetailProduct

urlpatterns = [
#    path('category/',CategoryView.as_view()),
#    path('book/',BookView.as_view()),
#    path('product/',ProductView.as_view()),

   path('categorygeneric/',ListCategory.as_view()),
   path('categorygeneric/<int:pk>/',DetailCategory.as_view()),
   path('bookgeneric/',ListBook.as_view()),
   path('bookgeneric/<int:pk>/',DetailBook.as_view()),
   path('productgeneric/',ListProduct.as_view()),
   path('productgeneric/<int:pk>/',DetailProduct.as_view())
]