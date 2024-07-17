from django.urls import path
from .views import post_list, create_post, delete_post, update_post

urlpatterns = [
    path('', post_list, name='list'),
    path('new/', create_post, name='create'),
    path('edit/<int:pk>/', update_post, name='update'),
    path('delete/<int:pk>/', delete_post, name='delete'),
]
