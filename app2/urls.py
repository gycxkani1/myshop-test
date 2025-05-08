from django.urls import path
from . import views

urlpatterns = [
    path('app2/index/', views.index, name='app2/index'),
]