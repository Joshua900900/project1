from django.urls import path
from .views import welcome_page, product_list

urlpatterns = [
    path('', welcome_page, name='welcome_page'),  
    path('products/', product_list, name='product_list'),  
  
]
