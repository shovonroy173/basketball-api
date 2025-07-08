from django.db import models
from django.conf import settings

# Create your models here.
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class TeamInformation(models.Model):
    opponent_team_name = models.CharField(max_length=100)
    jersey_color = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    circuit_or_level = models.CharField(max_length=100)
    game_date = models.DateField()
    performance_note = models.TextField(blank=True)
    youtube_link = models.URLField(blank=True, null=True, help_text="Paste YouTube video link")
    uploaded_video = models.FileField(upload_to='game_videos/', blank=True, null=True)

    def __str__(self):
        return f"{self.opponent_team_name}"
    


class TeamScouting(models.Model):
    report_title = models.CharField(max_length=200, help_text="Title of the scouting report")
    overview = models.TextField()
    strengths = models.JSONField(default=list, help_text="List of strengths")
    weaknesses = models.JSONField(default=list, help_text="List of weaknesses")
    key_players = models.TextField()
    tendencies = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, help_text="Report creation date and time")
    update_at = models.DateTimeField(auto_now=True, help_text="Report last updated date and time")

    def __str__(self):
        return self.report_title
    class Meta:
        verbose_name = "Team Scouting Report"
        verbose_name_plural = "Team Scouting Reports"