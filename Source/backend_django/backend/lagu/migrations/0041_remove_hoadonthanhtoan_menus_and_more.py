# Generated by Django 4.2.5 on 2023-10-21 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lagu', '0040_alter_hoadoncoctien_ngay_thanh_toan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoadonthanhtoan',
            name='menus',
        ),
        migrations.AlterField(
            model_name='hoadoncoctien',
            name='ngay_thanh_toan',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 22, 0, 23, 34, 844838)),
        ),
    ]
