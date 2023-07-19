from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),  # 根 URL 映射到 create 视图函数
    path('read/<int:record_id>/', views.read, name='read'),
    path('update/<int:record_id>/', views.update, name='update'),
    path('delete/<int:record_id>/', views.delete, name='delete'),
]

