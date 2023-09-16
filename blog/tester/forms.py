
# from django import forms
# from .models import HealthSurvey

# class HealthSurveyForm(forms.ModelForm):
#     class Meta:
#         model = HealthSurvey
#         fields = [
#             'cigarettes_per_day',
#             'exercise_per_week',
#             'reaction_time_ms',
#             'alcohol_per_week',
#             'sitting_duration_per_day'
#         ]
from django import forms
from .models import PersonInfo, HealthInfo, MiscInfo

class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = '__all__'

class HealthInfoForm(forms.ModelForm):
    class Meta:
        model = HealthInfo
        fields = '__all__'

class MiscInfoForm(forms.ModelForm):
    class Meta:
        model = MiscInfo
        fields = '__all__'
