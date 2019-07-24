from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from stackoverflow_clone.forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
