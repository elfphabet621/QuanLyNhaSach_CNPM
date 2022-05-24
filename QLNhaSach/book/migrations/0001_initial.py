# Generated by Django 4.0.3 on 2022-05-24 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ho_ten', models.CharField(max_length=100, null=True, verbose_name='Họ tên')),
                ('ngay_sinh', models.DateField(auto_now_add=True, null=True, verbose_name='Ngày sinh')),
                ('so_dien_thoai', models.CharField(max_length=13, null=True, verbose_name='Số điện thoại')),
                ('dia_chi', models.CharField(max_length=1000, null=True, verbose_name='Địa chỉ')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='Email')),
                ('chuc_vu', models.CharField(choices=[('nhân viên', 'nhân viên'), ('thủ kho', 'thủ kho'), ('chủ nhà sách', 'chủ nhà sách'), ('khách hàng', 'khách hàng')], max_length=100, null=True, verbose_name='Chức vụ')),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Thành viên',
            },
        ),
        migrations.CreateModel(
            name='Sach',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ten_sach', models.CharField(max_length=100, null=True)),
                ('ngay_nhap', models.DateField(null=True)),
                ('so_luong', models.IntegerField(null=True)),
                ('the_loai', models.CharField(max_length=100, null=True)),
                ('tac_gia', models.CharField(max_length=100, null=True)),
                ('don_gia', models.FloatField(null=True)),
                ('gia_ban', models.FloatField(null=True)),
                ('nha_xuat_ban', models.CharField(max_length=100, null=True)),
                ('nam_xuat_ban', models.IntegerField(null=True)),
                ('nguoi_nhap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book.person')),
            ],
            options={
                'verbose_name_plural': 'Sách',
            },
        ),
    ]
