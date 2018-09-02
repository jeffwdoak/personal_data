from django.urls import path

from . import views

app_name = 'exercise'
urlpatterns = [
    path('', views.exercise_index_view, name='index'),
    path('<int:year>/<str:month>/<int:day>/',
        views.ExerciseArchiveDayView.as_view(), name='archive_day'),
    path('add/', views.ExerciseCreate.as_view(), name='add'),
]
