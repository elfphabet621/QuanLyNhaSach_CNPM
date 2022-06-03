# Generated by Django 4.0.3 on 2022-05-31 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_remove_person_chuc_vu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_dau', models.FloatField(null=True)),
                ('phat_sinh', models.FloatField(null=True)),
                ('khach_hang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='book.person')),
            ],
        ),
    ]