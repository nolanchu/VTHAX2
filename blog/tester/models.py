from django.db import models

class MyModel(models.Model):
    data = models.JSONField()
from django.core.validators import MaxValueValidator
class PersonInfo(models.Model):
    AGE_CHOICES = [(i, str(i)) for i in range(1, 121)]
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

class ConsumptionInfo(models.Model):
    smoking = models.PositiveSmallIntegerField()
    alcohol = models.PositiveSmallIntegerField()
    diet = models.PositiveSmallIntegerField(validators=[MaxValueValidator])
    water = models.DecimalField(max_digits=5, decimal_places=2)

class PhysicalActivityInfo(models.Model):
    exercise = models.PositiveSmallIntegerField() # hours 
    desk = models.PositiveSmallIntegerField() # hours at
    MY_CHOICES = (
        ('a', 'Human-powered transport'),
        ('b', 'Motorized transport'),
    )
    transportation = models.CharField(max_length=1, choices=MY_CHOICES)

class BiologicalInfo(models.Model):
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    sleep = models.PositiveSmallIntegerField()
    sunscreen = models.BooleanField()

class MentalHealthInfo(models.Model):
    friends = models.PositiveSmallIntegerField()  # num of close friends
    STRESS_CHOICES = [(i, str(i)) for i in range(1, 11)]
    stress = models.PositiveSmallIntegerField(choices=STRESS_CHOICES)

class MiscInfo(models.Model):
    EDUCATION_CHOICES = [('HS', 'High School'), ('UG', 'Undergraduate'), ('PG', 'Postgraduate')]
    driving_safety = models.BooleanField()
    location_crime_rate = models.BooleanField()  # True for High, False for Low
    education_level = models.CharField(max_length=2, choices=EDUCATION_CHOICES)
