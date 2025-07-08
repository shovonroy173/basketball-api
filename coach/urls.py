from django.urls import path
from .views import *

urlpatterns = [
    path('team/information/', TeamInformationListCreateView.as_view(), name='team-information-list'),
    path('team/scouting/', TeamScoutingListCreateView.as_view(), name='team-scouting-list'),
    ]
