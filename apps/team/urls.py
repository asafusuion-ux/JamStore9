from django.urls import path 
from apps.team.views import TeamView


urlpatterns = [
    path('team/', TeamView.as_view(), name='team'),
]
