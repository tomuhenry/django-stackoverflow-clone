from django.db import models
# from django.contrib.auth.models import User
from questions.models import Question
from django.contrib.auth import get_user_model

# Create your models here.
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = get_user_model()
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.answer_text

