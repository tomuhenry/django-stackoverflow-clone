from django import forms
from . import models


class AnswerForm(forms.ModelForm):
    answer_text = forms.Textarea()
    answer_text.widget = forms.Textarea(
        attrs={
            'class': "form-control",
            'rows': 4,
            'placeholder': "Give answer here!"
        }
    )

    class Meta:
        model = models.Answer
        fields = [
            'answer_text',
        ]
