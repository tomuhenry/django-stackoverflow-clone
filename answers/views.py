from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models, forms
from questions.models import Question
from django.http import HttpResponseRedirect

@login_required
def create_answer(request, question_pk):
    form = forms.AnswerForm()
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid:
            answer = form.save(commit=False)
            answer.question = question.pk
            answer.save()
            messages.success(request, "Answer sent successfully")
            return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))
    return render(request, 'answers/answer-form.html', {'form': form})