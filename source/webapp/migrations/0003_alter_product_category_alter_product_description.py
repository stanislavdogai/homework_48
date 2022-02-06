# Generated by Django 4.0.1 on 2022-02-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_product_options_alter_product_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Разное'), ('milk', 'Молочная продукция'), ('meat', 'МЯСО'), ('vegetables', 'Овощи'), ('drink', 'Напитки')], default='other', max_length=15, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание'),
        ),
    ]
