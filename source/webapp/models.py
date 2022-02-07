from django.db import models
from django.urls import reverse

CATEGORY = [('other', 'Разное'), ('milk', 'Молочная продукция'), ('meat', 'МЯСО'), ('vegetables', 'Овощи'), ('drink', 'Напитки')]

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=15, default='other', choices=CATEGORY, verbose_name='Категория')
    remainder = models.PositiveIntegerField(null=False, blank=False, verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False, verbose_name='Цена')

    def __str__(self):
        return f'{self.pk}. {self.name}'

    def get_absolute_url(self):
        return reverse('product_index')

    class Meta:
        db_table = 'products'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Basket(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.PROTECT, related_name='basket', verbose_name='Продукты')
    amount = models.PositiveIntegerField(null=False, blank=False, verbose_name='Количество')

    def __str__(self):
        return f'{self.product} --- {self.amount}'

    class Meta:
        db_table = 'Basket'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    @property
    def sum_product(self):
        return self.amount * self.product.price




class Order(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')
    phone = models.CharField(max_length=15, null=False, blank=False, verbose_name='Номер телефона')
    address = models.CharField(max_length=50, null=False, blank=False, verbose_name='Адрес')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    def __str__(self):
        return f'ID {self.pk}. Дата: {self.date.date()} * Имя: {self.name} * Телефон: {self.phone} * Адрес: {self.address}'

    class Meta:
        db_table = 'Order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date']

class OrderBasketProduct(models.Model):
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE, related_name='orderbasket', verbose_name='Заказ')
    product = models.ForeignKey('webapp.Product', on_delete=models.PROTECT, related_name='productbasket', verbose_name='Продукт')
    amount = models.PositiveIntegerField(null=False, blank=False, verbose_name='Количество')

    def __str__(self):
        return f'Заказ: {self.order}  *  Продукт: {self.product.name}  *  Количество: {self.amount}'

    class Meta:
        db_table = 'ORDERBASKET'
        verbose_name = 'Промежуточная'
        verbose_name_plural = 'Промежуточная'

