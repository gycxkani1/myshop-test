from django.urls import path,re_path
from . import views
from app2.views_class import *

urlpatterns = [
    path('app2/index/', views.index, name='app2_index'),
    path('app2/show/<int:id>/', views.show, name='app2_show'),
    path('app2/article/<uuid:id>/', views.show_uuid, name='app2_show_uuid'),
    path('app2/article/<slug:q>/', views.show_slug, name='app2_show_slug'),
    re_path(r'app2/list/(?P<year>\d{4})/', views.article_list, name='app2_article_list'),
    re_path(r'app2/page/(?P<page>\d+)&key=(?P<key>\w+)/', views.article_page, name='app2_article_page'),
    path('app2/url_reverse/', views.url_reverse, name='app2_url_reverse'),
    path('app2/hello/', views.hello, name='app2_hello'),
    path('app2/test_get/', views.test_get, name='app2_test_get'),
    path('app2/test_post/', views.test_post, name='app2_test_post'),
    path('app2/test_response/', views.test_response, name='app2_test_response'),
    path('app2/test_render/', views.test_render, name='app2_test_render'),
    path('app2/test_redirect_model/<int:id>/', views.test_redirect_model, name='app2_test_redirect_model'),
    path('app2/userinfo/<int:id>/', views.userinfo, name='app2_userinfo'),
    path('app2/test_redirect_views/<int:id>/', views.test_redirect_views, name='app2_test_redirect_views'),
    path('app2/test_redirect/', views.test_redirect, name='app2_test_redirect'),
    path('app2/index_page_fun/', views.index_page, name='app2_index_page_fun'),
    path('app2/index_page_class/', views.IndexPageView.as_view(), name='app2_index_page_class'),
    path('app2/TestTemplateView/', TestTemplateView.as_view(), name='app2_TestTemplateView'),
    path('app2/test_listview/', TestListView.as_view(), name='app2_TestListView'),
    path('app2/test_detailview/<int:userid>', TestDetailView.as_view(), name='app2_TestDetailView'),

]