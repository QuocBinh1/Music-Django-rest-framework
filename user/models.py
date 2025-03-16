from django.db import models

# Create your models here.
class User(models.Model):
    nd_manguoidung = models.CharField(max_length=11)
    nd_email = models.EmailField()
    nd_matkhau = models.CharField(max_length=50)
    nd_sodienthoai = models.CharField(max_length=20)


    def __str__(self):
        return self.name