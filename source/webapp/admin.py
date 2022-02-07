from django.contrib import admin

# Register your models here.
from webapp.models import Product, Basket, Order

#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']
#     list_filter = ['id']
#     fields = ['id', 'name', 'remainder', 'price']


admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Order)