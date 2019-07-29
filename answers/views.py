from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from questions.models import Question
from . import models, forms
from django.http import HttpResponseRedirect

@login_required
def create_answer(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    form = forms.AnswerForm
    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        print(form)
        if form.is_valid:
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question.pk
            print(answer.save())
            answer.save()
            messages.success(request, "Answer added successfully")
            return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))
        return render(request, 'answers/answer_form.html', {'form': form})