from django.urls import path
from .views import health_survey, DisplayRecordsView
urlpatterns = [
    path('health_survey/', health_survey, name='health_survey'),
    path('display_records/', DisplayRecordsView.as_view(), name='display_records'),  # Add this line
]
