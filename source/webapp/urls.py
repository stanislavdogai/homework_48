from django.urls import path

from webapp.views.basket import (BasketView, ProductAddBasket, BasketProductDelete)
from webapp.views.products import (ProductIndexView, ProductCreateView, ProductDetailView,
                                   ProductDeleteView, ProductUpdateView, ProductBusketView)

urlpatterns = [
    path('', ProductIndexView.as_view(), name='product_index'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/basket', ProductBusketView.as_view(), name='product_basket'),
    path('product/<int:pk>/add', ProductAddBasket.as_view(), name='product_add'),
    path('products/basket', BasketView.as_view(), name='basket'),
    path('products/basket/delete/<int:pk>', BasketProductDelete.as_view(), name='basket_delete'),

]