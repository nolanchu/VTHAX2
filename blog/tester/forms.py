
from django import forms
from .models import HealthSurvey

class HealthSurveyForm(forms.ModelForm):
    class Meta:
        model = HealthSurvey
        fields = [
            'cigarettes_per_day',
            'exercise_per_week',
            'reaction_time_ms',
            'alcohol_per_week',
            'sitting_duration_per_day'
        ]
