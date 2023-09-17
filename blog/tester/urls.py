from django.urls import path
# from .views import health_survey, DisplayRecordsView
# urlpatterns = [
#     path('health_survey/', health_survey, name='health_survey'),
#     path('display_records/', DisplayRecordsView.as_view(), name='display_records'),  # Add this line
# ]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('display/', views.DisplayRecordsView.as_view()),
    path('step/6', views.finished),
    path('step/<str:step_num>', views.step),
    path('finished/', views.finished, name='finished'),  # You'll need to create this view
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

