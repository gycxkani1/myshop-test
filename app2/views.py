from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View

from app2.models import UserBaseInfo

# Create your views here.
def index(request):
    # return render(request,'index.html')
    return HttpResponse('app2中的index方法')

def show(request, id):
    return HttpResponse('app2中的show方法，参数id为：' + str(id))

def show_uuid(request, id):
    return HttpResponse('app2中的show_uuid方法，参数id为：' + str(id))
def show_slug(request, q):
    return HttpResponse('app2中的show_slug方法，参数q为：' + str(q))

def article_list(request,year):
    return HttpResponse('app2中的article_list方法，参数为year，指定4位，值为：' + str(year))

def article_page(request,page,key):
    return HttpResponse('app2中的article_page方法，参数page，任意数字，值为：' + str(page) + '，参数key，字母数字下划线，值为：' + key)
def url_reverse(request):
    # 使用reverse()方法反向解析url
    print("在views()函数中使用reverse()方法反向解析url的结果：" + reverse("app2_url_reverse"))
    return render(request,'2/url_reverse.html')

def hello(request):
    return HttpResponse('hello,Django!')

def test_get(request):
    print(request.get_host())                    # 域名 + 端口
    print(request.get_raw_uri())                 # 全部路径，包含参数
    print(request.path)                          # 获取访问文件路径，不含参数
    print(request.get_full_path())               # 获取访问文件路径，包含参数
    print(request.method)                        # 获取访问方法
    print(request.GET)                           # 获取GET请求参数
    print(request.META["HTTP_USER_AGENT"])       # 获取用户代理信息
    print(request.META["REMOTE_ADDR"])           # 获取用户IP地址
    print(request.GET.get('username'))           # 获取GET请求参数username
    return HttpResponse("测试get方法成功！")

def test_post(request):
    print(request.method)                       # 获取访问方法
    print(request.POST.get('username'))         # 获取POST请求参数username
    return render(request,'2/test_post.html')   # 返回一个html页面

def test_response(request):
    response=HttpResponse()
    # response.write("<h1>这是HttpResponse的测试</h1>")
    # response.write("<br>")
    response.write("hello django!")
    response.write("<br>")
    response.write(response.content)
    response.write("<br>")
    response.write(response['Content-type'])
    response.write("<br>")
    response.write(response.status_code)
    response.write("<br>")
    response.write(response.charset)
    response.write("<br>")
    return  response

def test_render(request):
    return render(request,'2/test_render.html',{'info':'hello  django!'},content_type='text/html;charset=utf-8')

def test_redirect_model(request,id):
    user=UserBaseInfo.objects.get(id=id)
    return redirect(user)

def userinfo(request,id):
    user=UserBaseInfo.objects.get(id=id)
    return HttpResponse("编号："+str(user.id)+"，用户名："+user.username+"，密码："+user.password+"，邮箱："+user.email+"，手机号："+user.phone+"，状态："+user.status+"，创建时间："+str(user.create_time))

def test_redirect_views(request,id):
    return redirect('app2_userinfo',id)

def test_redirect(request):
    return redirect('https://www.baidu.com/')  # 重定向到指定的URL

def index_page(request):
    '''
    视图函数
    '''
    if request.method ==  'GET':
        return HttpResponse('这是GET方法')
    elif request.method == 'POST':
        return HttpResponse('这是POST方法')
    
class IndexPageView(View):
    '''
    视图类
    '''
    def get(self,request):
        return HttpResponse('这是GET方法')
    def post(self,request):
        return HttpResponse('这是POST方法')