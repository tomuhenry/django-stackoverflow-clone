from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models, forms
from django.http import HttpResponseRedirect
from questions.models import Question


def answer_list(request, question_pk):
    answers = get_object_or_404(models.Answer, question_pk=question_pk)
    return render(request, 'questions/question_detail.html', {'answers': answers})


@login_required
def create_answer(request, question_pk):
    form = forms.AnswerForm()
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid:
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            messages.success(request, "Question created successfully")
            return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))
    return render(request, 'questions/question_form.html', {'form': form})
