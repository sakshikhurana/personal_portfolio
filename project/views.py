from django.shortcuts import render, reverse
from .models import Project
from django.views.generic import ListView
# Create your views here.


class HomeView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'home.html'
