# Generated by Django 4.2.5 on 2023-10-12 00:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lagu', '0029_alter_giamgia_ma_giam_gia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dsdatban',
            old_name='Ma_dat_ban',
            new_name='ma_dat_ban',
        ),
        migrations.AlterField(
            model_name='giamgia',
            name='ma_giam_gia',
            field=models.CharField(blank=True, default='RERB48', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='hoadoncoctien',
            name='ngay_thanh_toan',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 7, 36, 11, 741340)),
        ),
        migrations.AlterField(
            model_name='hoadonthanhtoan',
            name='ma_hoa_don',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
