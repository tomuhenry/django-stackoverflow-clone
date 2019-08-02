from django.urls import path

from . import views

app_name = "answers"

urlpatterns = [
    path('<question_pk>/answer/', views.create_answer, name="answer"),
]