from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_designers,
         name='all_designers'),
    path('designers-alphabetical/',
         views.all_designers_alphabetical,
         name='all_designers_alphabetical'),
    path('designer-detail/<designer_id>/',
         views.individual_designer,
         name='individual_designer'),
]
