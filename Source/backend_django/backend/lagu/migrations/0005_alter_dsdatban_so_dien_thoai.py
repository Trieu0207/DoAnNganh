# Generated by Django 4.2.5 on 2023-10-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lagu', '0004_menu_is_trang_thai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dsdatban',
            name='so_dien_thoai',
            field=models.CharField(max_length=10),
        ),
    ]