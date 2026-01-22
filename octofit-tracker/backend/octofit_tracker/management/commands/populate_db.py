from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        
        self.stdout.write('Creating superhero users...')
        
        # Create Marvel superheroes
        iron_man = User.objects.create(
            username='ironman',
            email='tony.stark@marvel.com',
            first_name='Tony',
            last_name='Stark'
        )
        iron_man.set_password('avengers123')
        iron_man.save()
        
        captain_america = User.objects.create(
            username='captainamerica',
            email='steve.rogers@marvel.com',
            first_name='Steve',
            last_name='Rogers'
        )
        captain_america.set_password('avengers123')
        captain_america.save()
        
        black_widow = User.objects.create(
            username='blackwidow',
            email='natasha.romanoff@marvel.com',
            first_name='Natasha',
            last_name='Romanoff'
        )
        black_widow.set_password('avengers123')
        black_widow.save()
        
        thor = User.objects.create(
            username='thor',
            email='thor.odinson@marvel.com',
            first_name='Thor',
            last_name='Odinson'
        )
        thor.set_password('avengers123')
        thor.save()
        
        hulk = User.objects.create(
            username='hulk',
            email='bruce.banner@marvel.com',
            first_name='Bruce',
            last_name='Banner'
        )
        hulk.set_password('avengers123')
        hulk.save()
        
        # Create DC superheroes
        batman = User.objects.create(
            username='batman',
            email='bruce.wayne@dc.com',
            first_name='Bruce',
            last_name='Wayne'
        )
        batman.set_password('justiceleague123')
        batman.save()
        
        superman = User.objects.create(
            username='superman',
            email='clark.kent@dc.com',
            first_name='Clark',
            last_name='Kent'
        )
        superman.set_password('justiceleague123')
        superman.save()
        
        wonder_woman = User.objects.create(
            username='wonderwoman',
            email='diana.prince@dc.com',
            first_name='Diana',
            last_name='Prince'
        )
        wonder_woman.set_password('justiceleague123')
        wonder_woman.save()
        
        flash = User.objects.create(
            username='flash',
            email='barry.allen@dc.com',
            first_name='Barry',
            last_name='Allen'
        )
        flash.set_password('justiceleague123')
        flash.save()
        
        aquaman = User.objects.create(
            username='aquaman',
            email='arthur.curry@dc.com',
            first_name='Arthur',
            last_name='Curry'
        )
        aquaman.set_password('justiceleague123')
        aquaman.save()
        
        self.stdout.write('Creating teams...')
        
        # Create Team Marvel
        team_marvel = Team.objects.create(name='Team Marvel')
        team_marvel.members.set([iron_man, captain_america, black_widow, thor, hulk])
        team_marvel.save()
        
        # Create Team DC
        team_dc = Team.objects.create(name='Team DC')
        team_dc.members.set([batman, superman, wonder_woman, flash, aquaman])
        team_dc.save()
        
        self.stdout.write('Creating activities...')
        
        # Create activities for Marvel heroes
        Activity.objects.create(
            user=iron_man,
            activity_type='Running',
            duration=45,
            calories_burned=450,
            date=date.today() - timedelta(days=1)
        )
        
        Activity.objects.create(
            user=captain_america,
            activity_type='Weight Training',
            duration=60,
            calories_burned=500,
            date=date.today() - timedelta(days=1)
        )
        
        Activity.objects.create(
            user=black_widow,
            activity_type='Martial Arts',
            duration=90,
            calories_burned=700,
            date=date.today()
        )
        
        Activity.objects.create(
            user=thor,
            activity_type='Hammer Lifting',
            duration=120,
            calories_burned=1000,
            date=date.today()
        )
        
        Activity.objects.create(
            user=hulk,
            activity_type='Smashing',
            duration=30,
            calories_burned=800,
            date=date.today() - timedelta(days=2)
        )
        
        # Create activities for DC heroes
        Activity.objects.create(
            user=batman,
            activity_type='Combat Training',
            duration=90,
            calories_burned=750,
            date=date.today()
        )
        
        Activity.objects.create(
            user=superman,
            activity_type='Flying',
            duration=60,
            calories_burned=600,
            date=date.today() - timedelta(days=1)
        )
        
        Activity.objects.create(
            user=wonder_woman,
            activity_type='Sword Fighting',
            duration=75,
            calories_burned=650,
            date=date.today()
        )
        
        Activity.objects.create(
            user=flash,
            activity_type='Speed Running',
            duration=30,
            calories_burned=900,
            date=date.today() - timedelta(days=1)
        )
        
        Activity.objects.create(
            user=aquaman,
            activity_type='Swimming',
            duration=120,
            calories_burned=850,
            date=date.today()
        )
        
        self.stdout.write('Creating workouts...')
        
        # Create workout suggestions
        workout1 = Workout.objects.create(
            name='Superhero Strength Training',
            description='Build strength like a superhero with compound exercises',
            difficulty='Hard'
        )
        workout1.suggested_for.set([captain_america, batman, wonder_woman])
        
        workout2 = Workout.objects.create(
            name='Speed and Agility Drills',
            description='Improve your speed and reflexes',
            difficulty='Medium'
        )
        workout2.suggested_for.set([flash, black_widow])
        
        workout3 = Workout.objects.create(
            name='Endurance Swimming',
            description='Build cardiovascular endurance through swimming',
            difficulty='Medium'
        )
        workout3.suggested_for.set([aquaman])
        
        workout4 = Workout.objects.create(
            name='Flight Training',
            description='High-intensity interval training for flying heroes',
            difficulty='Easy'
        )
        workout4.suggested_for.set([superman, iron_man, thor])
        
        workout5 = Workout.objects.create(
            name='Power Lifting',
            description='Maximum strength building for the strongest heroes',
            difficulty='Hard'
        )
        workout5.suggested_for.set([hulk, thor, superman])
        
        self.stdout.write('Creating leaderboard...')
        
        # Create leaderboard entries based on total calories burned
        leaderboard_data = [
            (thor, 1000, 1),
            (flash, 900, 2),
            (aquaman, 850, 3),
            (hulk, 800, 4),
            (batman, 750, 5),
            (black_widow, 700, 6),
            (wonder_woman, 650, 7),
            (superman, 600, 8),
            (captain_america, 500, 9),
            (iron_man, 450, 10),
        ]
        
        for user, score, rank in leaderboard_data:
            Leaderboard.objects.create(user=user, score=score, rank=rank)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with superhero test data!'))
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
