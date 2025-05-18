from django.urls import path,include,re_path
from . import views

urlpatterns = [
  path('user_reg/', views.user_reg, name='app6_user_reg'),
  path('user_login/', views.user_login, name='app6_user_login'),

]
