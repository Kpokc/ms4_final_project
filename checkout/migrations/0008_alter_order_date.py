# Generated by Django 3.2.8 on 2021-11-04 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20211104_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.SlugField(blank=True, default=datetime.datetime.now),
        ),
    ]
