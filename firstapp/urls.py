from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create, name='create'),
    path('read/<int:record_id>/', views.read, name='read'),
    path('update/<int:record_id>/', views.update, name='update'),
    path('delete/<int:record_id>/', views.delete, name='delete'),
]
