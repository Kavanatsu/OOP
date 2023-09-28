from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterUserForm


def ApplicationAllListView(request):
    return render(request, 'index.html')


def ApplicationListView(request):
    return render(request, 'profile.html')


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

