from django.urls import path,re_path
from . import views

urlpatterns = [
    path('app3/var/',views.var,name='app3_var'),
    path('app3/for_label/',views.for_label,name='app3_for_label'),
    path('app3/filter/',views.filter,name='app3_filter'),
    path('app3/html_filter/',views.html_filter,name='app3_html_filter'),
    path('app3/diy_filter/',views.diy_filter,name='app3_diy_filter'),
    path('app3/diy_tags/',views.diy_tags,name='app3_diy_tags'),
    path('app3/show_info/',views.show_info,name='app3_show_info'),
]