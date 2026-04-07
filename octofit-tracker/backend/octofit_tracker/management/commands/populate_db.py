from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel', is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel', is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc', is_superhero=True)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc', is_superhero=True)

        # Activities
        Activity.objects.create(user=tony.email, activity_type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=steve.email, activity_type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user=bruce.email, activity_type='swim', duration=25, date='2023-01-03')
        Activity.objects.create(user=clark.email, activity_type='fly', duration=60, date='2023-01-04')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='10x100m sprints', difficulty='medium')
        Workout.objects.create(name='Deadlifts', description='5x5 heavy deadlifts', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
