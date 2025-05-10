from django.db import models

# Create your models here.

class Championship(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    season = models.CharField(max_length=20)  # e.g., "2023/2024"

    def __str__(self):
        return f"{self.name} ({self.season})"

class Team(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    championship = models.ForeignKey(Championship, related_name='teams', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ranking(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='ranking')
    played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.points} points"
