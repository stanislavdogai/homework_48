from django.db import models

CATEGORY = [('none', 'Разное'), ('milk', 'Молочная продукция'), ('meat', 'МЯСО'), ('vegetables', 'Овощи'), ('drink', 'Напитки')]
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    category = models.CharField(max_length=15, default='other', choices=CATEGORY, verbose_name='Категория')
    remainder = models.PositiveIntegerField(null=False, blank=False, verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False, verbose_name='Цена')

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        db_table = 'products'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'