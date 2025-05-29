from rest_framework import viewsets
from rest_framework import mixins
from app8.custommodelviewset import CustomModelViewSet
from app8.models import *
from app8.serializers import *
from app8.mypage import *
from app8.myfilter import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from common.permissions import IsOwnerOrReadOnly
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class GoodsViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
        返回所有数据.
    retrieve:
        返回单条数据实例.
    """
    queryset = Goods.objects.all() # 查询集
    serializer_class = GoodsSerializer # 序列化类
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly) # 权限类, 需要权限才能访问


class GoodsView(CacheResponseMixin,viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = MyPage # 自定义分页类
    filter_backends = (DjangoFilterBackend,) # 指定过滤器的配置类
    # filter_fields = ('name', 'price') # 过滤字段为商品名和价格
    filterset_class = GoodsFilter # 指定过滤器的自定义配置类

    #搜索
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields=('name','price')
    #排序
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    ordering_fields=('id','name','price')

# class GoodsDetailViewSet(CacheResponseMixin,viewsets.ReadOnlyModelViewSet):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

class GoodsView_Custom(CacheResponseMixin,CustomModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class=MyPage
    filter_backends = (DjangoFilterBackend,)
    #filter_fields = ('name', 'price')
    filterset_class=GoodsFilter
    #permission_classes=(permissions.IsAuthenticated,IsOwnerOrReadOnly)
    #搜索
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields=('name','price')
    #排序
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    ordering_fields=('id','name','price')


