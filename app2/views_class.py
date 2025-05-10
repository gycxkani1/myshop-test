from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView
from .models import *

class TestTemplateView(TemplateView):
    # 指定模板文件
    template_name = '2/test_templateview.html'
    # 重写父类的get_context_data方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 增加模板变量info
        context['info'] = '该变量可以传递到模板'
        return context
    
class TestListView(ListView):
    # 指定模型
    model = UserBaseInfo
    # 指定模板文件
    template_name = '2/test_listview.html'
    # 指定变量名
    context_object_name = 'users'
    # 指定分页
    paginate_by = 2
    # queryset = UserBaseInfo.objects.filter(status='1')
    # 重写父类的get_queryset方法
    def get_queryset(self):
        # 返回状态为1的数据
        userinfo = UserBaseInfo.objects.filter(status='1')
        return userinfo
    # 重写父类的get_context_data方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 增加模板变量info
        context['info'] = 'ListView变量可以传递到模板'
        print(context)
        return context
    
class TestDetailView(DetailView):
    model = UserBaseInfo
    template_name = '2/test_detailview.html'
    context_object_name = 'users' # 指定变量名
    pk_url_kwarg = 'userid'  # 指定URL中主键参数的名称
    # 重写父类的get_object方法
    # def get_object(self):
    #     userinfo = UserBaseInfo.objects.filter(status='1')
    #     return userinfo