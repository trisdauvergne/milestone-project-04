from django.urls import path
from .import views

urlpatterns = [
    path('create-profile/', views.create_profile, name='create_profile'),
    path('order-history/', views.order_history, name='order_history'),
]
