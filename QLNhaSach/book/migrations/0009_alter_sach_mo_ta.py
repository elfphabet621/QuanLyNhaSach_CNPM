# Generated by Django 4.0.3 on 2022-05-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_sach_mo_ta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sach',
            name='mo_ta',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Mô tả ngắn'),
        ),
    ]