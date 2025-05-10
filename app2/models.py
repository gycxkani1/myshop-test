from django.db import models
from django.urls import reverse

# Create your models here.
class UserBaseInfo(models.Model):
    """
    用户基本信息表
    """
    id = models.AutoField(verbose_name='编号',primary_key=True)
    username = models.CharField(max_length=30, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    status  = models.CharField(max_length=1, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, db_column='createDate',verbose_name='创建时间')
    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("app2_userinfo", kwargs={"id": self.pk})
    

    class Meta:
        db_table = 'userBaseInfo2'
        verbose_name = '用户基本信息表'
        verbose_name_plural = '用户基本信息表'  # admin后台显示名称