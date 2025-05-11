from django.db import models

# Create your models here.
class UserBaseInfo(models.Model):
    """
    用户基本信息表
    """
    id = models.AutoField(verbose_name='编号',primary_key=True)
    username = models.CharField(max_length=30, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    status  = models.CharField(max_length=1, verbose_name='状态')
    createdate = models.DateTimeField(db_column='createDate',verbose_name='创建日期')
    def __str__(self):
        return str(self.id)
     
    class Meta:
        managed = False
        db_table = 'userBaseInfo4'
        verbose_name = '用户基本信息表'
        verbose_name_plural = '用户基本信息表'  # admin后台显示名称