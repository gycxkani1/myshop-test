from django.db import models

# Create your models here.

class ImgFile(models.Model):
    """
    图片文件
    """
    name=models.CharField(max_length=30,verbose_name='名称',default='')
    headimg=models.FileField(upload_to='uploads/',verbose_name='文件名')
    # upload_time=models.DateTimeField(auto_now_add=True,verbose_name='上传时间')
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = '用户头像信息'
        # verbose_name_plural = '图片文件'
        db_table = 'user_img'
