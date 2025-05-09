from django.urls import path
from . import views

urlpatterns = [
    path('app1/index/', views.index, name='app1_index'),
]