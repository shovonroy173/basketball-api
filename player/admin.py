from django.contrib import admin
from .models import *

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'player_name',
        'jersey_number',
        'position',
        'team',
        'class_year',
        'gender',
        'opponent_team_name',
        'tournament_name', 'game_result', 'opponent_faced', 'score_or_margin'
    )
    list_filter = ('team', 'gender', 'class_year', 'position')
    search_fields = ('player_name__full_name', 'opponent_team_name', 'team')
    autocomplete_fields = ['player_name']



@admin.register(PlayerReport)
class PlayerReportAdmin(admin.ModelAdmin):
    list_display = (
        'player_name',
        'field_goal_percentage',
        'rebounds',
        'assists',
        'steals_and_blocks'
    )
    search_fields = ('player_name__full_name', )
    list_filter = ('field_goal_percentage', )
    readonly_fields = ('strengths', 'weaknesses')  # Optional: make JSONFields readonly

    fieldsets = (
        ('Report Info', {
            'fields': ('report_title',)
        }),
        ('Player Info', {
            'fields': ('player_name',)
        }),
        ('Performance Details', {
            'fields': (
                'field_goal_percentage',
                'rebounds',
                'assists',
                'steals_and_blocks'
            )
        }),
        ('Analysis', {
            'fields': (
                'overview',
                'projection',
                'strengths',
                'weaknesses'
            )
        }),
    )