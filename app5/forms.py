from django import forms
import re
from django.core.exceptions import ValidationError

from app5.models import *

def age_validate(value):
    if value < 1 or value > 120:
        raise ValidationError('年龄只能在1-120之间')
    
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[0-9]|17[6-8]|18[0-9]|19[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class UserInfoForm(forms.Form):
    '''用户状态'''
    STATUS = ((None,'请选择'),(0,'正常'),(1,'无效'),)
    username = forms.CharField(
        label='用户名',
        min_length=6,
        max_length=30,
        required=True,
        widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'})
        )
    password = forms.CharField(
        label='密码',
        min_length=6,
        max_length=20,
        required=True,
        widget=forms.widgets.PasswordInput(attrs={'class':'password','placeholder':'请输入密码'},render_value=True)
        )
    age=forms.IntegerField(
        label='年龄',
        initial=1,
        required=True,
        widget=forms.widgets.NumberInput(attrs={'class':'form-control','placeholder':'请输入年龄'})
        )
    mobile=forms.CharField(
        label='手机号',
        min_length=11,
        max_length=11,
        required=True,
        widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入手机号'})
        )
    status=forms.ChoiceField(
        label='状态',
        required=True,
        choices=STATUS,
        widget=forms.widgets.Select(attrs={'class':'form-control','placeholder':'请输入状态'})
        )
    createdate=forms.DateTimeField(
        label='创建日期',
        required=False,
        widget=forms.widgets.DateTimeInput(attrs={'class':'form-control','placeholder':'请输入创建日期'})
        )


class UserInfo_Msg_Form(forms.Form):
    '''用户状态'''
    STATUS = ((None,'请选择'),(0,'正常'),(1,'无效'),)
    username = forms.CharField(
        label='用户名',
        min_length=6,
        max_length=30,
        required=True,
        widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}),
        error_messages={
            'required':'用户名不能为空',
            'min_length':'用户名长度不能小于6位',
            'max_length':'用户名长度不能大于30位',
            
        }
        )
    password = forms.CharField(
        label='密码',
        min_length=6,
        max_length=20,
        required=True,
        widget=forms.widgets.PasswordInput(attrs={'class':'password','placeholder':'请输入密码'},render_value=True),
        error_messages={
            'required':'密码不能为空',
            'min_length':'密码长度不能小于6位',
            'max_length':'密码长度不能大于20位'
        }
        )
    age=forms.IntegerField(
        label='年龄',
        initial=1,
        required=True,
        widget=forms.widgets.NumberInput(attrs={'class':'form-control','placeholder':'请输入年龄'}),
        validators=[age_validate],
        error_messages={
            'required':'年龄不能为空',
            
        }
        )
    mobile=forms.CharField(
        label='手机号',
        min_length=11,
        max_length=11,
        required=True,
        widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入手机号'}),
        validators=[mobile_validate],
        error_messages={
            'required':'手机号不能为空',
            'min_length':'长度不能小于11位',
            'max_length':'长度不能大于11位'
            
        }
        )
    status=forms.ChoiceField(
        label='状态',
        required=True,
        choices=STATUS,
        widget=forms.widgets.Select(attrs={'class':'form-control','placeholder':'请输入状态'}),
        error_messages={'required':'状态不能为空'}
        )
    createdate=forms.DateTimeField(
        label='创建日期',
        required=False,
        widget=forms.widgets.DateTimeInput(attrs={'class':'form-control','placeholder':'请输入创建日期'})
        )

class ImgFileForm(forms.Form):
    '''用户头像'''
    name=forms.CharField(
        label='名称',
        min_length=1,
        max_length=30,
        required=True,
        widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入名称'}),
        error_messages={
            'required':'名称不能为空',
            'min_length':'名称长度不能小于1位',
            'max_length':'名称长度不能大于30位'
        }
        )
    headimg=forms.FileField(
        label='文件',
        required=True,
        widget=forms.widgets.FileInput(attrs={'class':'form-control'}),
        error_messages={'required':'文件不能为空'}
        )

class UserBaseInfoModelForm(forms.ModelForm):

    confirm_password = forms.CharField(
        label='确认密码', widget=forms.PasswordInput(attrs={"class": "password"}, render_value=True),
        error_messages={
            'required': '密码不能为空',
        })

    class Meta:
         # 定义关联模型
        model = UserBaseInfo
        # 定义需要在表单中展示的字段。
        fields = ['username', 'password', 'confirm_password', 'age', 'mobile', 'status']
        # 如果要显示全部字段，可以如下设置
        # fields="__all__"
         # 如果Models中定义了名称，这里不用再定义
        labels = {
            "age": "最佳年龄",
            "mobile": "手机信息",
        }
        widgets = {
            # 文本框渲染为密码输入框
            "password": forms.widgets.PasswordInput(attrs={"class": "password"}, render_value=True)
        }
        error_messages = {
            "username": {
                'required': '用户姓名不能为空',
                'min_length': '长度最少6位',
                'invalid': '输入正确的用户姓名'
            },
            "password": {
                'max_length': '密码最长10位',
                'required': '密码不能为空',
                'min_length': '密码最少6位'
            },
            "age": {
                'required': '年龄不能为空',
            },
            "mobile": {
                'required': '手机号码不能为空',
            },
            "status": {
                'required': '用户状态不能为空',
            }
        }
    # 校验手机号码的局部钩子函数
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        print(mobile)
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(mobile):
            raise ValidationError('手机号码格式错误')
        return mobile
    
    # 校验年龄的局部钩子函数
    def clean_age(self):
        age = self.cleaned_data.get('age')
        print(age)
        if age < 1 or age > 120:
            raise ValidationError('年龄只能在1-120之间')
        return age
    
    # 校验用户名的局部钩子函数
    def clean_username(self):
        username = self.cleaned_data.get('username')
        print(username)
        if len(username) < 6 or len(username) > 30:
            raise ValidationError('用户名的长度只能在6-30之间')
        return username
    
    # 校验密码的局部钩子函数
    def clean_password(self):
        password = self.cleaned_data.get('password')
        print(password)
        if len(password) < 6 or len(password) > 20:
            raise ValidationError('密码的长度只能在6-20之间')
        return password
    
     # 校验确认密码的局部钩子函数
    def clean_confirm_password(self):
        # password =  self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get('confirm_password')
        print(confirm_password)
        if len(confirm_password) < 6 or len(confirm_password) > 20:
            raise ValidationError('确认密码的长度只能在6-20之间')
        # if password != confirm_password:
        #     raise forms.ValidationError("二次密码输入不一致")
        return confirm_password

    # 全局钩子函数
    def clean(self):
        password =  self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("二次密码输入不一致")

