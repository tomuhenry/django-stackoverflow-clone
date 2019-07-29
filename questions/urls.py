from django.urls import path

from . import views

app_name = "questions"

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('create_question/', views.create_question, name="create_question"),
    path('<pk>/', views.question_detail, name='question_detail'),
    path('edit_question/<pk>', views.edit_question, name="edit_question"),
    path('delete/<pk>', views.delete_question, name="delete_question"),

]