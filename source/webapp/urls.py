from django.urls import path

from webapp.views.products import ProductIndexView, ProductCreateView, ProductDetailView, ProductDeleteView, \
    ProductUpdateView

urlpatterns = [
    path('', ProductIndexView.as_view(), name='product_index'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
]