from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_prints, name='all_prints'),
    path('add-print/', views.add_print, name='add_print'),
    path('large-print/<print_id>/', views.large_print, name='large_print'),
    path('edit-print/<print_id>/', views.edit_print, name='edit_print'),
    path('delete-print/<print_id>/', views.delete_print, name='delete_print'),
]