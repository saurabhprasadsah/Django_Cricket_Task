from django.test import TestCase
from .models import Team, Player, Match

class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            identifier=1,
            name='Team A',
            logo_uri='http://example.com/logo.png',
            club_state='State A'
        )

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Team A')

class MatchModelTest(TestCase):
    def setUp(self):
        self.team1 = Team.objects.create(identifier=1, name='Team A', logo_uri='http://example.com/logo.png', club_state='State A')
        self.team2 = Team.objects.create(identifier=2, name='Team B', logo_uri='http://example.com/logo.png', club_state='State B')
        self.match = Match.objects.create(team1=self.team1, team2=self.team2)

    def test_match_str(self):
        self.assertEqual(str(self.match), 'Match between Team A and Team B')
