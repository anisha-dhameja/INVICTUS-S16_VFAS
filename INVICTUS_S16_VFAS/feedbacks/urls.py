from django.urls import path
from . import views

app_name = "feedbacks"
urlpatterns = [
    path('<str:slug>/feedback-form/<int:number_of_questions>/', views.feedback_form, name="feedback-form"),
    path('<str:slug>/feedback-form/', views.feedback_form, name="feedback-form"),
]
