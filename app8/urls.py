from django.urls import path,include,re_path

from app8 import views,views_api_view,views_apiview


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



]