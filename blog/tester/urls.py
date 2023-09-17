from django.urls import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.home),
    path('display/', views.DisplayRecordsView.as_view()),
    path('references/', views.references),
    path('step/6', views.finished),
    path('step/<str:step_num>', views.step),
    path('finished/', views.finished, name='finished'),  # You'll need to create this view
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

