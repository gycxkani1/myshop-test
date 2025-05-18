from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import  login,logout,authenticate
from django.urls import reverse

# Create your views here.


def user_reg(request):
    if request.method == "GET":
        return render(request, '6/user_reg.html')
    if request.method == "POST":
        uname = request.POST.get('username','')
        pwd = request.POST.get('password','')
        email = request.POST.get('email','')
        if User.objects.filter(username=uname):
            info = "用户名已存在"
        else:
            d = dict(username=uname, password=pwd,email=email,is_staff=1,is_active=1,is_superuser=1)
            user = User.objects.create_user(**d)
            info = "注册成功，请登录"
            #跳转到登陆页面
            return redirect(reverse("app6_user_login"))
            # return render(request,'6/user_login.html')
        return render(request, '6/user_reg.html', {'info': info})

def user_login(request):
    if request.method == "GET":
        return render(request,'6/user_login.html')
    if request.method == "POST":
        uname = request.POST.get('username','') # 获取用户名
        pwd = request.POST.get('password','') # 获取密码
        if User.objects.filter(username=uname): # 用户名存在
            user = authenticate(username=uname,password=pwd) # 验证用户名和密码
            if user: # 用户名和密码正确
                if user.is_active: # 用户已激活
                    login(request,user) # 登陆
                    info = "登陆成功"
                    return render(request,'6/index.html',{'info':info})
                else:
                    info = "用户未激活"  
            else:
                info = "用户名或密码错误"
        else:
            info = "用户不存在"
        return render(request,'6/user_login.html',{'info':info})