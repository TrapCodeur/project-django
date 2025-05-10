from django.urls import path
from . import views

urlpatterns = [
    path('championships/', views.championship_list, name='championship_list'),  # Liste des championnats
    path('championships/<int:championship_id>/', views.championship_detail, name='championship_detail'),  # Détails d'un championnat
    path('championships/<int:championship_id>/teams/', views.team_list, name='team_list'),  # Liste des équipes d'un championnat
    path('championships/<int:championship_id>/rankings/', views.ranking_list, name='ranking_list'),  # Classements d'un championnat
]
