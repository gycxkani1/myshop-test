from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import  login,logout,authenticate
from django.urls import reverse
from app6.models import MyUser
from django.contrib.auth.decorators import login_required, permission_required


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
    
def myuser_reg(request):
    if request.method == "GET":
        return render(request, '6/user_reg.html')
    if request.method == "POST":
        uname = request.POST.get('username','')
        pwd = request.POST.get('password','')
        email = request.POST.get('email','')
        weChat = request.POST.get('weChat','')
        level = request.POST.get('level','')
        if MyUser.objects.filter(username=uname):
            info = "用户名已存在"
        else:
            d = dict(username=uname, password=pwd,email=email,is_staff=1,is_active=1,is_superuser=1,weChat=weChat,level=level)
            user = MyUser.objects.create_user(**d) # 创建用户
            info = "注册成功，请登录"
            #跳转到登陆页面
            # return redirect(reverse("app6_myuser_login"))
            # return render(request,'6/user_login.html')
        return render(request, '6/user_reg.html', {'info': info})
    
def myuser_login(request):
    if request.method == "GET":
        return render(request,'6/user_login.html')
    if request.method == "POST":
        uname = request.POST.get('username','') # 获取用户名
        pwd = request.POST.get('password','') # 获取密码
        if MyUser.objects.filter(username=uname): # 用户名存在
            user = authenticate(username=uname,password=pwd) # 验证用户名和密码
            if user: # 用户名和密码正确
                if user.is_active: # 用户已激活
                    login(request,user) # 登陆
                    info = "登陆成功"
                    return redirect(reverse("app6_user_index")) # 跳转到用户首页
                    # return render(request,'6/index.html',{'info':info})
                else:
                    info = "用户未激活"  
            else:
                info = "用户名或密码错误"
        else:
            info = "用户不存在"
        return render(request,'6/user_login.html',{'info':info})
    
def myuser_logout(request):
    logout(request)
    return redirect(reverse("app6_myuser_login"))

@permission_required("app6.change_myuser")
@login_required
def myuser_edit(request):
    return render(request,'6/user_edit.html')


@permission_required("app6.view_myuser")
@login_required
def user_index(request):
    users=MyUser.objects.all()
    return render(request,'6/user_index.html',{'users':users})

def test(request):
    return HttpResponse("我也执行了")
