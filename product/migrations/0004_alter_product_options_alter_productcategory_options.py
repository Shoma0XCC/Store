# Generated by Django 5.1.3 on 2025-01-27 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Categorie', 'verbose_name_plural': 'Categories'},
        ),
    ]
