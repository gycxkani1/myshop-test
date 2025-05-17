from django.urls import path,include,re_path
# from django.templatetags.static import static
# from django.views.static import serve
from app5 import views
# from myshop import settings


urlpatterns = [
    path('upload_file/', views.upload_file, name='upload_file'),
    path('userinfo_form/', views.userinfo_form, name='userinfo_form'),
    path('userinfo_msg_form/', views.userinfo_msg_form, name='userinfo_msg_form'),
    path('imgfileform/', views.imgfileform, name='imgfileform'),
    path('userbaseinfo_modelform/', views.userbaseinfo_modelform, name='userbaseinfo_modelform'),
    path('ajax_login/',views.ajax_login, name='ajax_login'),
    path('ajax_login_data/',views.ajax_login_data, name='ajax_login_data'),

    
]