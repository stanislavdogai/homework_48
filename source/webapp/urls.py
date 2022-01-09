from django.urls import path

from webapp.views import home_page, product_view

urlpatterns = [
    path('', home_page, name='home_page'),
    path('product/<int:pk>/', product_view, name='product_view')
]