from django.db import models
# from django.utils import timezone
# import datetime

# Create your models here.
class Sach(models.Model):
    id = models.CharField(max_length=100, null=True)
    ten_sach = models.CharField(max_length=100, null=True)
    ngay_nhap = models.DateField(auto_now_add=True, primary_key=True)
    nguoi_nhap = models.CharField(max_length=100, null=True)
    so_luong = models.IntegerField(null=True)
    the_loai = models.CharField(max_length=100, null=True)
    tac_gia = models.CharField(max_length=100, null=True)
    don_gia = models.FloatField(null=True)
    gia_ban = models.FloatField(null=True)
    nha_xuat_ban = models.CharField(max_length=100, null=True)
    nam_xuat_ban = models.IntegerField(null=True)
    
    def __str__(self):
	    return f'{self.ten_sach}_{self.ngay_nhap}'
    
    # class Meta: # vì django ko cho tạo PK 2 thuộc tính nên làm cách này
    #     unique_together = ('id', 'ngay_nhap',)

# class NhanVien(models.Model):
#     id = models.CharField(max_length=100, primary_key=True)
#     ho_ten = models.CharField(max_length=100, null=True)
#     ngay_sinh = models.DateField(auto_now_add=True, null=True)
#     so_dien_thoai = models.CharField(max_length=13, null=True)
#     dia_chi = models.CharField(max_length=1000, null=True)
#     email = models.CharField(max_length=50, null=True)
#     chuc_vu = models.CharField(max_length=100, null=True)
    
#     def __str__(self):
# 	    return self.ho_ten