from django import forms
from . import models

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'answer_text'
        ]