from django.db import models

class MyModel(models.Model):
    data = models.JSONField()
# from django.core.validators import MaxValueValidator
class PersonInfo(models.Model):
    AGE_CHOICES = [(i, str(i)) for i in range(1, 121)]
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

class ConsumptionInfo(models.Model):
    smoking = models.PositiveSmallIntegerField()
    alcohol = models.PositiveSmallIntegerField()
    DIET_CHOICES = [(i, str(i)) for i in range(8)]
    diet = models.PositiveSmallIntegerField(choices=DIET_CHOICES)
    water = models.DecimalField(max_digits=5, decimal_places=2)

class PhysicalActivityInfo(models.Model):
    exercise = models.PositiveSmallIntegerField() # hours 
    desk = models.PositiveSmallIntegerField() # hours at
    MY_CHOICES = (
        (1, 'Human-powered transport'),
        (0, 'Motorized transport'),
    )
    transportation = models.PositiveSmallIntegerField(choices=MY_CHOICES)

class BiologicalInfo(models.Model):
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    sleep = models.PositiveSmallIntegerField()
    # sunscreen = models.()

class MentalHealthInfo(models.Model):
    friends = models.PositiveSmallIntegerField()  # num of close friends
    # STRESS_CHOICES = [(i, str(i)) for i in range(1, 11)]
    STRESS_CHOICES = [(2, "Low"), (1, "Moderate"), (0, "High")]
    stress = models.PositiveSmallIntegerField(choices=STRESS_CHOICES)

class MiscInfo(models.Model):
    EDUCATION_CHOICES = [(4, 'Postgraduate'), (3, 'Completed Undergraduate'), (2, 'Current Undergraduate'), (1, 'Completed High School'), (0, 'Less than High School')]
    DRIVING_CHOICES = [(2, 'Very Safe'), (1, 'Moderately Safe'), (0, 'Unsafe')]
    driving_safety = models.PositiveSmallIntegerField(choices=DRIVING_CHOICES)
    CRIME_CHOICES = [(4, "Very Low"), (3, "Low"), (2, "Moderate"), (1, "High")]
    location_crime_rate = models.PositiveSmallIntegerField(choices=CRIME_CHOICES)
    education_level = models.PositiveSmallIntegerField(choices=EDUCATION_CHOICES)
