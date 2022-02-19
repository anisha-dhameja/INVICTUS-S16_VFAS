from django.urls import path
from . import views
app_name = "events"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('details/', views.details, name="details"),
]
