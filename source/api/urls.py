from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api import views
from api.views import BasketAddAPIView, BasketProductDelete, BasketProductRemove, BasketList

product_routers = routers.DefaultRouter()
product_routers.register(r'product', views.ProductViewSet)

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(product_routers.urls)),
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add_basket/', BasketAddAPIView.as_view(), name='add_product_to_basket'),
    path('baskets/', BasketList.as_view(), name='basket_list'),
    path('delete_product_basket/', BasketProductDelete.as_view(), name='delete_product_from_basket'),
    path('remove_product_basket/', BasketProductRemove.as_view(), name='delete_product_from_basket')
]