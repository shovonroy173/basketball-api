from rest_framework import serializers
from .models import *

class TeamInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInformation
        fields = '__all__'


class TeamScoutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamScouting
        fields = '__all__'
