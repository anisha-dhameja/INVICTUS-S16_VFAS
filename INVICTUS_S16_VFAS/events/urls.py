from django.urls import path
from . import views
app_name = "events"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('details/<str:slug>', views.details, name="details"),
]
 