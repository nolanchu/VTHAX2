from django.db import models

class HealthSurvey(models.Model):
    cigarettes_per_day = models.PositiveIntegerField()
    exercise_per_week = models.DurationField()  # Saved as timedelta, e.g., 3 hours 30 minutes
    reaction_time_ms = models.PositiveIntegerField()
    alcohol_per_week = models.PositiveIntegerField()  # e.g., in units
    sitting_duration_per_day = models.DurationField()
