from django.db import models
from django.contrib.auth.models import User
from questions.models import Question


class Answer(models.Model):
    answer_text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text

    class Meta:
        ordering = ["-created_at"]
        managed = True
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
