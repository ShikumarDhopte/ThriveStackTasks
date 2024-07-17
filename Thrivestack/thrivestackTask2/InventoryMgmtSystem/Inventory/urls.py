from django.urls import path
from .views import item_list, add_item, delete_item, update_item

urlpatterns = [
    path('', item_list, name='list'),
    path('new/', add_item, name='create'),
    path('edit/<int:pk>/', update_item, name='update'),
    path('delete/<int:pk>/', delete_item, name='delete'),
]
