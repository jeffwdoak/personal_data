from django.db import models


class Exercise(models.Model):
    time = models.DateTimeField()
    exercise = models.CharField(max_length=200)
    amount = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True)
    units = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return ' '.join([str(self.time), self.exercise])


