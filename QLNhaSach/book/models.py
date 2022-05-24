from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import random
import uuid

# Create your models here.
class Person(models.Model):
    class Meta:
        verbose_name_plural = 'Thành viên'
        
    list_chucvu = (
			('nhân viên', 'nhân viên'),
			('thủ kho', 'thủ kho'),
            ('chủ nhà sách', 'chủ nhà sách'),
            ('khách hàng', 'khách hàng')
			) 
    id = models.CharField(max_length=100, primary_key=True, editable=True)
    ho_ten = models.CharField('Họ tên', max_length=100, null=True)
    ngay_sinh = models.DateField('Ngày sinh', auto_now_add=True, null=True)
    so_dien_thoai = models.CharField('Số điện thoại', max_length=13, null=True)
    dia_chi = models.CharField('Địa chỉ', max_length=1000, null=True)
    email = models.CharField('Email', max_length=50, null=True)
    chuc_vu = models.CharField('Chức vụ', max_length=100, null=True, choices=list_chucvu)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    
    def __str__(self):
	    return self.id
 
class Sach(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    ten_sach = models.CharField(max_length=100, null=True)
    ngay_nhap = models.DateField(null=True)
    so_luong = models.IntegerField(null=True)
    the_loai = models.CharField(max_length=100, null=True)
    tac_gia = models.CharField(max_length=100, null=True)
    don_gia = models.FloatField(null=True)
    gia_ban = models.FloatField(null=True)
    nha_xuat_ban = models.CharField(max_length=100, null=True)
    nam_xuat_ban = models.IntegerField(null=True)
    nguoi_nhap = models.ForeignKey(Person, null=True, on_delete=models.CASCADE) # models.CharField(max_length=100, null=True)
    
    def __str__(self):
	    return f'{self.ten_sach}_{self.ngay_nhap}'
    
    def clean(self):
        if self.nguoi_nhap.chuc_vu != 'thủ kho':
            raise ValidationError('người nhập phải là thủ kho!')
        
    class Meta: # vì django ko cho tạo PK 2 thuộc tính nên làm cách này
        # unique_together = ('id', 'ngay_nhap',)
        verbose_name_plural = "Sách"

class HoaDon(models.Model):
    class Meta:
        verbose_name_plural = 'Hóa đơn'
        
    pttt = (
            ('Thẻ ngân hàng', 'Thẻ ngân hàng'),
            ('Tiền mặt', 'Tiền mặt'),
            )
    id_HD = models.CharField('Mã hóa đơn', max_length=100, primary_key=True, default= 'HD_', editable=True)
    ngay_lap_HD = models.DateTimeField(null=True, auto_now_add=True, editable=True)
    tong_tien = models.FloatField(null=True)
    nguoi_lap_HD = models.ForeignKey(Person, verbose_name='Nhân viên', null=True, blank=True, related_name="nhan_vien", on_delete=models.CASCADE)
    khach_hang = models.ForeignKey(Person, verbose_name='Khách hàng', null=True, blank=True, related_name="khach_hang", on_delete=models.CASCADE)
    phuong_thuc_thanh_toan = models.CharField('Phương thức thanh toán', max_length=100, null=False, choices=pttt)
    
    def __str__(self):
	    return self.id_HD
    
    def clean(self):
        if self.khach_hang.chuc_vu != 'khách hàng':
            raise ValidationError('khách hàng không có trong database')
        if self.nguoi_lap_HD.chuc_vu != 'nhân viên':
            raise ValidationError('người lập hóa đơn phải là nhân viên!')