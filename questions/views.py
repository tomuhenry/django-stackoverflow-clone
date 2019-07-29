from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models, forms
from answers.forms import AnswerForm
from answers.models import Answer
from django.http import HttpResponseRedirect


def question_list(request):
    questions = models.Question.objects.all()
    return render(request, 'questions/question_list.html', {'questions': questions})


def question_detail(request, pk):
    question = get_object_or_404(models.Question, pk=pk)
    answers = Answer.objects.all().filter(question_id=pk)
    return render(request, 'questions/question_detail.html', {
        'question': question,
        'answers':answers,
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
    if request.user == question.author:
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
    else:
        messages.error(request, "You do not have right to edit this question")
        return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))


@login_required
def delete_question(request, pk):
    question = get_object_or_404(models.Question, pk=pk)
    question.delete()
    messages.info(request, "Question deleted")
    return HttpResponseRedirect(reverse_lazy('questions:question_list'))

# @login_required
# def create_answer(request, pk):
#     question = get_object_or_404(models.Question, pk=pk)
#     form = AnswerForm
#     print(form)
#     if request.method == "POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid:
#             answer = form.save(commit=False)
#             answer.author = request.user
#             answer.question = question.pk
#             answer.save()
#             messages.success(request, "Answer added successfully")
#             return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'pk': question.pk}))
#         return render(request, 'answers/answer_form.html', {'form': form})