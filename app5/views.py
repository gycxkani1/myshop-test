import os
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def upload_file(request):
    if request.method=="GET":
        return render(request,"5/upload.html")
    # 在请求方法为POST时进行处理，文件上传为POST请求
    if request.method=="POST":
        # 获取上传的文件，如果没有文件，则默认为None
        myFile=request.FILES.get("myfile",None)
        if myFile:
            # 打开特定的文件进行二进制的写操作
            path='media/uploads/'
            if not os.path.exists(path):
                os.makedirs(path)
            dest=open(os.path.join(path+myFile.name),'wb+')
            for chunk in myFile.chunks(): # 分块写入文件
                dest.write(chunk)
                dest.close()
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")


from .forms import *
def userinfo_form(request):
    if request.method=="GET":
        myform=UserInfoForm()
        return render(request,"5/userinfo.html",{"form_obj":myform})
    if request.method=="POST":
        myform=UserInfoForm(request.POST)
        if myform.is_valid():
            # print(form.cleaned_data)
            return HttpResponse("提交成功")
        else:
            return render(request,"5/userinfo.html",{"form_obj":myform})
        
def userinfo_msg_form(request):
    if request.method=="GET":
        myform=UserInfo_Msg_Form()
        return render(request,"5/userinfoform.html",{"form_obj":myform})
    else:
        f=UserInfo_Msg_Form(request.POST)
        if f.is_valid():
            print(f.clean()) # 获取所有字段数据，以字典格式返回
            print(f.cleaned_data["username"]) #  获取指定字段数据
            print(f.data) # 获取所有字段数据，以QueryDict字典格式返回
        else:
            errors=f.errors
            print(errors)
            return render(request,"5/userinfoform.html",{"form_obj":f,"errors":errors})
        return  render(request,"5/userinfoform.html",{"form_obj":f})

def imgfileform(request):
    if request.method=="GET":
        myform=ImgFileForm()
        return render(request,"5/upload_form.html",{"form_obj":myform})
    else:
        f=ImgFileForm(request.POST,request.FILES)
        if f.is_valid():
            name = f.cleaned_data["name"]
            headimg = f.cleaned_data["headimg"]
            userimg = ImgFile()
            userimg.name=name
            userimg.headimg=headimg
            userimg.save()
            print("上传成功")
            return render(request,"5/upload_form.html",{"form_obj":f,'user':userimg})