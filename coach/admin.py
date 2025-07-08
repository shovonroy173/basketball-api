from django.contrib import admin
from .models import *

@admin.register(TeamInformation)
class TeamInformationAdmin(admin.ModelAdmin):
    list_display = (
        'opponent_team_name', 
        'jersey_color', 
        'gender', 
        'circuit_or_level', 
        'game_date'
    )
    list_filter = ('gender', 'circuit_or_level', 'game_date')
    search_fields = ('opponent_team_name', 'jersey_color', 'circuit_or_level')
    ordering = ('-game_date',)


@admin.register(TeamScouting)
class TeamScoutingAdmin(admin.ModelAdmin):
    list_display = (
        'report_title', 
        'overview', 
        'create_at', 
        'update_at'
    )
    search_fields = ('report_title', 'overview')
    list_filter = ('create_at', 'update_at')
    ordering = ('-create_at',)