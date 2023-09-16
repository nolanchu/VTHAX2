from django import forms
from .models import PersonInfo, MentalHealthInfo, PhysicalActivityInfo, BiologicalInfo, ConsumptionInfo, MiscInfo

class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = '__all__'

class MentalHealthForm(forms.ModelForm):
    class Meta:
        model = MentalHealthInfo
        fields = '__all__'

class PhysicalActivityInfoForm(forms.ModelForm):
    class Meta:
        model = PhysicalActivityInfo
        fields = '__all__'

class BiologicalInfoForm(forms.ModelForm):
    class Meta:
        model = BiologicalInfo
        fields = '__all__'

class ConsumptionInfoForm(forms.ModelForm):
    class Meta:
        model = ConsumptionInfo
        fields = '__all__'

class MiscInfoForm(forms.ModelForm):
    class Meta:
        model = MiscInfo
        fields = '__all__'
