from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    photo=models.CharField('用户头像',max_length=50)
    weChat=models.CharField('微信号',max_length=30)
    level=models.IntegerField('用户等级',default=1)

    def __str__(self):
        return self.username
    class Meta(AbstractUser.Meta):
        permissions = (
           ['check_myuser','审核用户信息'],
        )