# Generated by Django 4.2.5 on 2023-10-08 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lagu', '0014_alter_giamgia_ma_giam_gia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giamgia',
            name='ma_giam_gia',
            field=models.CharField(default='GG0001', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='hoadoncoctien',
            name='ngay_thanh_toan',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 22, 56, 37, 113980)),
        ),
    ]
