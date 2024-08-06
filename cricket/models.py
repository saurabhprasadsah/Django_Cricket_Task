from django.db import models

class Team(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo_uri = models.URLField(max_length=200)
    club_state = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    identifier = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image_uri = models.URLField(max_length=200)
    jersey_number = models.IntegerField()
    country = models.CharField(max_length=100)
    matches = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    fifties = models.IntegerField(default=0)
    hundreds = models.IntegerField(default=0)
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name='won_matches', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name}"

class PointsTable(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.points} points"
