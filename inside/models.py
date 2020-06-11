from django.db import models
from django.contrib.auth.models import User as UserAdmin
# Create your models here.

class SanPham(models.Model):
    id=models.AutoField(primary_key=True)
    ten_san_pham=models.CharField('Ten san pham', max_length=200, unique=True)
    hinh = models.ImageField('Hinh', upload_to='hinh_san_pham', blank=True)
    don_gia_ban = models.FloatField('Don gia')
    mo_ta_tom_tat = models.CharField('Tom tat', max_length=200)
    chi_tiet = models.TextField('Chi tiet')
    trang_thai = models.BooleanField('Trang thai',blank=True, default=True)
    def __str__(self):
        return self.ten_san_pham

class User(models.Model):
    name = models.CharField(max_length=255, unique = True)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'User'

class UserProfileInfo(models.Model):
    user = models.OneToOneField(UserAdmin, on_delete=models.PROTECT)
    portfolio = models.URLField(blank = True)
    picture = models.ImageField(upload_to="images/", blank = True)

    def __str__(self):
        return self.user.username
