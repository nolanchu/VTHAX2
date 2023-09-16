from django.db import models

# class HealthSurvey(models.Model):
#     cigarettes_per_day = models.PositiveIntegerField()
#     exercise_per_week = models.DurationField()  # Saved as timedelta, e.g., 3 hours 30 minutes
#     reaction_time_ms = models.PositiveIntegerField()
#     alcohol_per_week = models.PositiveIntegerField()  # e.g., in units
#     sitting_duration_per_day = models.DurationField()

from django.db import models

class PersonInfo(models.Model):
    AGE_CHOICES = [(i, str(i)) for i in range(1, 121)]
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    smoking = models.BooleanField()
    alcohol = models.BooleanField()

class HealthInfo(models.Model):
    DIET_CHOICES = [('V', 'Vegetarian'), ('NV', 'Non-Vegetarian')]
    SLEEP_CHOICES = [(i, str(i)) for i in range(1, 25)]
    
    diet = models.CharField(max_length=2, choices=DIET_CHOICES)
    water_intake = models.PositiveSmallIntegerField()  # in litres
    physical_activity = models.PositiveSmallIntegerField()  # hours per week
    sleep = models.PositiveSmallIntegerField(choices=SLEEP_CHOICES)

class MiscInfo(models.Model):
    EDUCATION_CHOICES = [('HS', 'High School'), ('UG', 'Undergraduate'), ('PG', 'Postgraduate')]
    
    driving_safety = models.BooleanField()
    location_crime_rate = models.BooleanField()  # True for High, False for Low
    education_level = models.CharField(max_length=2, choices=EDUCATION_CHOICES)
