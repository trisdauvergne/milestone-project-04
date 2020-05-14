from django.urls import path
from .import views

urlpatterns = [
    path('', views.bag_contents, name='bag_contents'),
    path('add/<print_id>/', views.add_print_to_bag, name='add_print_to_bag'),
    path('adjust/<print_id>/', views.adjust_bag_quantity, name='adjust_bag_quantity'),
    path('remove-print/<print_id>/', views.remove_print, name='remove_print'),
]
