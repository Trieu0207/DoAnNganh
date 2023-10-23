# Generated by Django 4.2.5 on 2023-10-12 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lagu', '0027_alter_dsdatban_ma_dat_ban_alter_giamgia_ma_giam_gia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoadonthanhtoan',
            name='ma_hoa_don',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='giamgia',
            name='ma_giam_gia',
            field=models.CharField(blank=True, default='GGMKED', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='hoadoncoctien',
            name='ngay_thanh_toan',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 7, 29, 40, 995922)),
        ),
    ]
