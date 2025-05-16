from django.urls import path,include,re_path
from app4 import views
from myshop import settings
from django.templatetags.static import static
from django.views.static import serve

urlpatterns = [
    path('qs_all/', views.qs_all, name='qs_all'),
    path('qs_filter/', views.qs_filter, name='qs_filter'),
    path('qs_get/', views.qs_get, name='qs_get'),
    path('qs_exclude/', views.qs_exclude, name='qs_exclude'),
    path('qs_distinct/', views.qs_distinct, name='qs_distinct'),
    path('qs_values/', views.qs_values, name='qs_values'),

     path('q_func/', views.q_func, name='q_func'),

    path('userinfo_trans/', views.userinfo_trans, name='userinfo_trans'),
]
