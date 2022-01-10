from django.urls import path

from webapp.views import home_page, product_view, create_product, delete_product, update_product

urlpatterns = [
    path('', home_page, name='home_page'),
    path('product/<int:pk>/', product_view, name='product_view'),
    path('create/', create_product, name='create_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
    path('update/<int:pk>/', update_product, name='update_product'),
]