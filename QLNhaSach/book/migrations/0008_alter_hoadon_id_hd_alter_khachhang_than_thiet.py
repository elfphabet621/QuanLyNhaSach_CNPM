# Generated by Django 4.0.3 on 2022-05-24 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_remove_khachhang_dia_chi_remove_khachhang_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoadon',
            name='id_HD',
            field=models.CharField(default='HD_20568', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='khachhang',
            name='than_thiet',
            field=models.BinaryField(default=0, editable=True),
        ),
    ]