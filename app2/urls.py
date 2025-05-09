from django.urls import path,re_path
from . import views

urlpatterns = [
    path('app2/index/', views.index, name='app2_index'),
    path('app2/show/<int:id>/', views.show, name='app2_show'),
    path('app2/article/<uuid:id>/', views.show_uuid, name='app2_show_uuid'),
    path('app2/article/<slug:q>/', views.show_slug, name='app2_show_slug'),
    re_path(r'app2/list/(?P<year>\d{4})/', views.article_list, name='app2_article_list'),
    re_path(r'app2/page/(?P<page>\d+)&key=(?P<key>\w+)/', views.article_page, name='app2_article_page'),
    path('app2/url_reverse/', views.url_reverse, name='app2_url_reverse'),

]