# Generated by Django 3.2 on 2023-04-06 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_photo_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
    ]
