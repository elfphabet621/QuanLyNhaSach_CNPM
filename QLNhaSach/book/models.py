from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import random
import uuid

# Create your models here.
class NhanVien(models.Model):
    list_chucvu = (
			('nhân viên', 'nhân viên'),
			('thủ kho', 'thủ kho'),
            ('chủ nhà sách', 'chủ nhà sách'),
			) 
    id = models.CharField(max_length=100, primary_key=True)
    ho_ten = models.CharField('Họ tên', max_length=100, null=True)
    ngay_sinh = models.DateField('Ngày sinh', auto_now_add=True, null=True)
    so_dien_thoai = models.CharField('Số điện thoại', max_length=13, null=True)
    dia_chi = models.CharField('Địa chỉ', max_length=1000, null=True)
    email = models.CharField('Email', max_length=50, null=True)
    chuc_vu = models.CharField('Chức vụ', max_length=100, null=True, choices=list_chucvu)
    
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
    nguoi_nhap = models.ForeignKey(NhanVien, null=True, on_delete=models.SET_NULL) # models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.ten_sach}_{self.ngay_nhap}'
    
    def clean(self):
        if self.nguoi_nhap.chuc_vu != 'thủ kho':
            raise ValidationError('người nhập phải là thủ kho!')
        
#     class Meta: # vì django ko cho tạo PK 2 thuộc tính nên làm cách này
#         unique_together = ('id', 'ngay_nhap',)

class KhachHang(models.Model):
    # id = models.CharField(max_length=100,)
    ho_ten = models.CharField('Họ tên', max_length=100, null=True)
    so_dien_thoai = models.CharField('Số điện thoại', max_length=13, null=True)
    email = models.CharField('Email', max_length=50, null=True)
    # dia_chi = models.CharField('Địa chỉ', max_length=1000, null=True)
    ngay_lap_tk = models.DateTimeField(auto_now_add=True, null=True) # sau cùng nên thêm auto_now_add=True
    # than_thiet = models.BinaryField(default=0, editable=True)
    # user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE) # 1 khachhang chỉ có 1 tài khoản
    # profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    password = models.CharField('Mật khẩu', max_length=20, null=True) # nâng cấp: https://stackoverflow.com/questions/17523263/how-to-create-password-field-in-model-django
    
    def __str__(self):
        return self.ho_ten

class HoaDon(models.Model):
    pttt = (
            ('Thẻ ngân hàng', 'Thẻ ngân hàng'),
            ('Tiền mặt', 'Tiền mặt'),
            )
    id_HD = models.CharField(max_length=100, primary_key=True, default= 'HD_', editable=True)
    id_KH = models.ForeignKey(KhachHang, null=True, on_delete=models.SET_NULL)
    ngay_lap_HD = models.DateTimeField(null=True)
    tong_tien = models.FloatField(null=True)
    nguoi_lap_HD = models.ForeignKey(NhanVien, on_delete=models.PROTECT)
    phuong_thuc_thanh_toan = models.CharField('Phương thức thanh toán', max_length=100, null=False, choices=pttt)
    
    def __str__(self):
        return self.id_HD
    
    def clean(self):
        if self.nguoi_lap_HD.chuc_vu != 'nhân viên':
            raise ValidationError('người lập hóa đơn phải là nhân viên!')