"""
Tests of exercise/models.py

"""
import datetime

from django.test import TestCase
from django.utils import timezone

from exercise.models import Exercise

class ExerciseTestCase(TestCase):
    """
    Tests of Exercise model class

    """
    def setUp(self):
        Exercise.objects.create(
            time=datetime.datetime(2018, 8, 1, 12, 5, 0, tzinfo=timezone.utc),
            exercise='running',
            amount=15,
            units='min',
            notes='Hard run!',
            )
        Exercise.objects.create(
            time=datetime.datetime(2018, 8, 2, 12, 45, 0, tzinfo=timezone.utc),
            exercise='squat',
            amount=5,
            weight=135,
            units='lbs',
            )
        Exercise.objects.create(
            time=datetime.datetime(2018, 8, 2, 12, 45, 0, tzinfo=timezone.utc),
            exercise='squat',
            amount=5,
            weight=135,
            units='kgs',
            )

    def test_running_exercise_has_correct_fields(self):
        """Test construction of an Exercise object"""
        expected_fields = {
            'time': datetime.datetime(2018, 8, 1, 12, 5, 0,
                                      tzinfo=timezone.utc),
            'exercise': 'running',
            'amount': 15,
            'units': 'min',
            'notes': 'Hard run!',
            'weight': None,
            }
        running = Exercise.objects.get(exercise='running')
        actual_fields = {name:running.__dict__[name] for name in expected_fields}
        for name in expected_fields:
            self.assertEqual(expected_fields[name], actual_fields[name])

    def test_get_all_exercises(self):
        """Test class method to get list of all exercises"""
        expected_exercises = {'squat', 'running'}
        actual_exercises = Exercise.get_all_exercises()
        self.assertEqual(expected_exercises, actual_exercises)

    def test_get_all_units(self):
        """Test class method to get all units for a specified exercise"""
        exercise = 'squat'
        expected_units = {'lbs', 'kgs'}
        actual_units = Exercise.get_all_units(exercise)
        self.assertEqual(expected_units, actual_units)
