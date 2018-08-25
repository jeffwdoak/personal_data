"""
Views for exercise-tracking app.

"""
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DayArchiveView
from django.views.generic.edit import CreateView

from .models import Exercise

def exercise_index_view(request):
    five_days_ago = timezone.now() - datetime.timedelta(days=5)
    exercises = Exercise.objects.filter(time__gte=five_days_ago)
    days = exercises.datetimes('time', 'day').order_by('-datetimefield')
    exercises_by_day = []
    for day in days:
        day_tup = (day, exercises.filter(time__date=day).order_by('time'))
        exercises_by_day.append(day_tup)
    context = {'exercises_by_day': exercises_by_day}
    #context = {'exercise_list': exercises}
    return render(request, 'exercise/index.html', context)

class ExerciseArchiveDayView(DayArchiveView):
    queryset = Exercise.objects.all()
    date_field = 'time'
    allow_future = False
    template_name = 'exercise/archive_day.html'

class ExerciseCreate(CreateView):
    model = Exercise
    fields = ['time', 'exercise', 'amount', 'weight', 'units', 'notes']




# index - group exercises by date, and sort by time. show as exercise
# amount x weight (unit)


# add exercise - pull down menu for excercises populated by existing entries, or
# add new one, auto-populate date and time but allow changges, blank spots for
# amount and weight. autopopulate units based on most used units for the
# selected exercise, if present?
