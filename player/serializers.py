from rest_framework import serializers
from .models import Player, PlayerReport
from django.contrib.auth import get_user_model

User = get_user_model()

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name']
        read_only_fields = ['full_name']
    

class PlayerReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerReport
        fields = '__all__'

