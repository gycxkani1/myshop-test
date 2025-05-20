from django.urls import path,include,re_path
from . import views

urlpatterns = [
  path('user_reg/', views.user_reg, name='app6_user_reg'),
  path('user_login/', views.user_login, name='app6_user_login'),

  path('myuser_reg/', views.myuser_reg, name='app6_myuser_reg'),
  path('myuser_login/', views.myuser_login, name='app6_myuser_login'),
  path('myuser_logout/', views.myuser_logout, name='app6_myuser_logout'),
  path('user_index/', views.user_index, name='app6_user_index'),
  path('myuser_edit/', views.myuser_edit, name='app6_myuser_edit'),

  path('test/', views.test, name='app6_test'),
   

]
