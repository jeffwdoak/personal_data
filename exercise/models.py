"""
ORM models for Exercise app.

Main model is the Exercise class, which stores an exercise 'set' - a single set
of repetitions of weight lifting or areobic exercises.

"""

from django.db import models


class Exercise(models.Model):
    """
    Store an exercise 'set', defined by a single set of repetitions of weight
    lifting or an aerobic exercise. The exercise has a time, exercise, and
    amount associated with it. Optional fields include a weight, units for the
    amount or weight, and notes about the exercise.

    """
    time = models.DateTimeField()
    exercise = models.CharField(max_length=200)
    amount = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True)
    units = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return ' '.join([str(self.time), self.exercise])

    @classmethod
    def get_all_exercises(cls):
        """Get set of all exercises across all objects"""
        #all_exercises = cls.objects.values('exercise').distinct()
        #all_exercises = [query['exercise'] for query in all_exercises]
        all_exercises = cls.objects.values_list('exercise',
                                                flat=True).distinct()
        all_exercises = set(all_exercises)
        return all_exercises
