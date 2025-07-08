from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Gender choices
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class Player(models.Model):
    # Only allow users who are marked as players
    player_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_player': True},
        related_name='player_profiles'
    )

    jersey_number = models.PositiveIntegerField()
    height = models.FloatField(help_text="Height in cm or inches")
    position = models.CharField(max_length=50)
    class_year = models.CharField(max_length=10)
    game_context = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    opponent_team_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_images/', blank=True, null=True, help_text="Upload player image")
    performance_note = models.TextField(blank=True)

    tournament_name = models.CharField(max_length=255)
    game_result = models.CharField(max_length=50)
    opponent_faced = models.CharField(max_length=255)
    score_or_margin = models.CharField(max_length=50)
    game_flow_details = models.TextField()
    game_video = models.FileField(upload_to='game_videos/', blank=True, null=True, help_text="Upload game video if available")
    create_at = models.DateTimeField(auto_now_add=True, help_text="Scouting Context creation date and time")
    update_at = models.DateTimeField(auto_now=True, help_text="Scouting Context last updated date and time")

    def __str__(self):
        return f"{self.player_name.full_name} - #{self.jersey_number}"


class PlayerReport(models.Model):
    report_title = models.CharField(max_length=255, help_text="Title of the player report")
    player_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_player': True},
        related_name='player_reports',
        help_text="Select the player for whom the report is being created"
    )
    overview = models.TextField()
    strengths = models.JSONField(default=list, help_text="List of strengths")
    weaknesses = models.JSONField(default=list, help_text="List of weaknesses")
    projection = models.TextField()
    field_goal_percentage = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],help_text="Field Goal Percentage")
    rebounds = models.IntegerField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],help_text="Rebounds")
    assists = models.IntegerField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],help_text="Assists")
    steals_and_blocks = models.IntegerField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],help_text="Steals & Blocks")
    create_at = models.DateTimeField(auto_now_add=True, help_text="Report creation date and time")
    update_at = models.DateTimeField(auto_now=True, help_text="Report last updated date and time")

    def __str__(self):
        return f"{self.player_name.full_name}'s Report"