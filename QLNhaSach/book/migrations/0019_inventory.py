# Generated by Django 4.0.3 on 2022-06-10 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_alter_nhapsach_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_sach', models.CharField(max_length=100, null=True, verbose_name='Tên sách')),
                ('ton_dau', models.FloatField(null=True)),
                ('phat_sinh', models.FloatField(null=True)),
            ],
        ),
    ]
