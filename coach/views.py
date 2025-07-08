from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *
from .models import *

class TeamInformationListCreateView(generics.ListCreateAPIView):
    serializer_class = TeamInformationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or getattr(user, 'is_coach', False):
            return TeamInformation.objects.all()
        return TeamInformation.objects.all()


class TeamScoutingListCreateView(generics.ListCreateAPIView):
    serializer_class = TeamScoutingSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or getattr(user, 'is_coach', False):
            return TeamScouting.objects.all()
        return TeamScouting.objects.all()