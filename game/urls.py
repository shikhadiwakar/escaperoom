from django.urls import path
from . import views

urlpatterns = [
    path('animations/', views.animations_view, name='animations'),
    path('level/<int:level_id>/', views.level_view, name='level_view'),
    path('level/<int:level_id>/puzzle/<int:puzzle_id>/', views.puzzle_view, name='puzzle_view'),
    # Add more URLs for other views and functionalities
]
