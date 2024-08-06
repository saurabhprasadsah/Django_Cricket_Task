from django.shortcuts import render, get_object_or_404
from .models import Team, Player, Match, PointsTable
import random

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = team.players.all()
    return render(request, 'team_detail.html', {'team': team, 'players': players})

def generate_fixtures(request):
    teams = list(Team.objects.all())
    matches = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            match = Match(team1=teams[i], team2=teams[j])
            match.save()
            matches.append(match)
    random.shuffle(matches)
    return render(request, 'fixtures.html', {'matches': matches})


def points_table(request):
    points = PointsTable.objects.all().order_by('-points')
    return render(request, 'points_table.html', {'points': points})

