from django.test import TestCase
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(), username='testuser', email='testuser@example.com', password='password'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')

class TeamModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(), username='teamuser', email='teamuser@example.com', password='password'
        )
        self.team = Team.objects.create(_id=ObjectId(), name='Team Test')
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Team Test')
        self.assertIn(self.user, self.team.members.all())

class ActivityModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(), username='activityuser', email='activityuser@example.com', password='password'
        )
        self.activity = Activity.objects.create(
            _id=ObjectId(), user=self.user, activity_type='Running', duration=timedelta(minutes=30)
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, timedelta(minutes=30))

class LeaderboardModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(), username='leaderboarduser', email='leaderboarduser@example.com', password='password'
        )
        self.leaderboard = Leaderboard.objects.create(
            _id=ObjectId(), user=self.user, score=100
        )

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)
        self.assertEqual(self.leaderboard.user, self.user)

class WorkoutModelTestCase(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            _id=ObjectId(), name='Workout Test', description='Test Description'
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Workout Test')
        self.assertEqual(self.workout.description, 'Test Description')
