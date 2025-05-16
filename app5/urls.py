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
    
]