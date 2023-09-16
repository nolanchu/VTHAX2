from django.urls import path
# from .views import health_survey, DisplayRecordsView
# urlpatterns = [
#     path('health_survey/', health_survey, name='health_survey'),
#     path('display_records/', DisplayRecordsView.as_view(), name='display_records'),  # Add this line
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('step1/', views.step1, name='step1'),
    path('step2/', views.step2, name='step2'),
    path('step3/', views.step3, name='step3'),
    path('finished/', views.finished, name='finished'),  # You'll need to create this view
]

