# Generated by Django 3.2.12 on 2022-05-27 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_remove_sach_anh_bia_alter_sach_anh_sach_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='chuc_vu',
        ),
    ]
