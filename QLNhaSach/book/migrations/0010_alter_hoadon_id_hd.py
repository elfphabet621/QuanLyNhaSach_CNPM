# Generated by Django 4.0.3 on 2022-05-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_remove_khachhang_than_thiet_alter_hoadon_id_hd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoadon',
            name='id_HD',
            field=models.CharField(default='HD_', max_length=100, primary_key=True, serialize=False),
        ),
    ]
