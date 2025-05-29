from django.urls import path,include,re_path

from app8 import views,views_api_view,views_apiview, views_generics, views_mixins,views_viewset

from rest_framework.routers import DefaultRouter


goods_list=views_viewset.GoodsViewSet.as_view({
    'get':'list',
})

goods_detail=views_viewset.GoodsViewSet.as_view({
    'get': 'retrieve',
})

# 创建路由器并注册视图
router=DefaultRouter() 
router.register('goods5',views_viewset.GoodsViewSet)
router.register('goods_all',views_viewset.GoodsView)
# basename参数指定路由的基本名称，避免与其他视图冲突
router.register('goods_custom',views_viewset.GoodsView_Custom,basename="goods_custom")



urlpatterns = [
  path('goods/index/',views.GoodsListView.as_view(),name='app8-goods-index'),
  path('goods/list/',views.GoodsListView_JsonResponse.as_view(),name='app8-goods-list'),

  path('goods/',views.GoodsView.as_view()), # get post
  path('goods/<id>/',views.GoodsView.as_view()), # put delete
  #@api_view装饰器
  path('goods1/',views_api_view.GoodsList), # get post
  path('goods1/<id>/',views_api_view.GoodsList), # put delete
  #ApiView视图
  path('goods2/',views_apiview.GoodsView.as_view()), # get post
  path('goods2/<id>/',views_apiview.GoodsView.as_view()), # put delete
  #mixins
  path('goods3/',views_mixins.GoodsView.as_view()),
  path('goods3/<pk>/',views_mixins.GoodsDetailView.as_view()),
  #generics
  path('goods4/',views_generics.GoodsView.as_view()),
  path('goods4/<pk>/',views_generics.GoodsDetailView.as_view()),

  #GenericViewSet
  # path('goods5/',goods_list), # 获取或创建
  # path('goods5/<pk>/',goods_detail), # 查找、更新、删除
  # 还可以直接写在一行内
  # path('goods5/',views_viewset.GoodsViewSet.as_view({'get':'list',})),
  # path('goods5/<pk>',views_viewset.GoodsViewSet.as_view({'get': 'retrieve',})),

  #ModelViewSet
  path("",include(router.urls))



]