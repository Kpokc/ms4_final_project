# Generated by Django 3.2.8 on 2021-11-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.SlugField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.SlugField(default=0),
        ),
    ]
