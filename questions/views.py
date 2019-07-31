from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models, forms
from django.http import HttpResponseRedirect


def question_list(request):
    questions = models.Question.objects.all()
    return render(request, 'questions/question_list.html', {'questions': questions})


def question_detail(request, pk):
    question = get_object_or_404(models.Question, pk=pk)
    return render(request, 'questions/question_detail.html', {
        'question': question,
    })


@login_required
def create_question(request):
    form = forms.QuestionForm()
    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid:
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, "Question created successfully")
            return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))
    return render(request, 'questions/question_form.html', {'form': form})


@login_required
def edit_question(request, pk):
    question = get_object_or_404(models.Question, pk=pk)
    form_class = forms.QuestionForm
    form = form_class(instance=question)
    if request.method == "POST":
        form = form_class(request.POST, instance=question)
        if form.is_valid:
            form.save()
            messages.success(request, "Question updated successfully")
            return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))
    return render(request, 'questions/question_form.html', {
        'form': form,
        'question': question
    })


@login_required
def delete_question(request, pk):
    question = get_object_or_404(models.Question, pk=pk)
    question.delete()
    messages.success(request, "Question deleted")
    return HttpResponseRedirect(reverse_lazy('questions:question_list'))
