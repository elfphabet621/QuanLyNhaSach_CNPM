# Generated by Django 4.0.3 on 2022-06-09 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_alter_chitiethoadon_sach_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sach',
            name='ngay_nhap',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Ngày nhập'),
        ),
    ]
