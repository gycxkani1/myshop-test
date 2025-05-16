from django import forms
import re
from django.core.exceptions import ValidationError

from app5.models import ImgFile

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


    # class Meta:
    #     model = UserInfo
    #     fields = '__all__'


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
    class Meta:
        model = ImgFile
        fields = '__all__'