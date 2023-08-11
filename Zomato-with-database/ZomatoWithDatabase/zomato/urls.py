from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
    path('add_menu/', views.add_menu_item, name='add_menu_item'),
    path('update_item/<int:pk>/', views.update_menu_item, name='update_item'),
     path('delete_item/<int:pk>/', views.delete_menu_item, name='delete_item'),
     path('take_order/', views.take_order, name='take_order'),
]
