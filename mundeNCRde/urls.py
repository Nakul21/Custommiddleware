from . import views
from django.urls import path

urlpatterns = [
    path('', views.test_endpoint, name='test_endpoint'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),
    path('add_users', views.add_users, name='add_users'),
]
