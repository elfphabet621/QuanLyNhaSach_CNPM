# Generated by Django 4.0.3 on 2022-05-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_sach_don_gia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sach',
            name='don_gia',
            field=models.FloatField(null=True),
        ),
    ]