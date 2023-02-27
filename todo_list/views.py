from django.shortcuts import render
from . import models
from django.views.generic import ListView, TemplateView  #Listview creates a list of available objects in "object_list"
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class TaskListView(ListView):
    model = models.TodoList
    template_name = "list_task.html"


class TaskCreateView(CreateView):
    model = models.TodoList
    template_name = "create_task.html"
    fields = ("title", "description")


class TaskEditView(UpdateView):
    model = models.TodoList
    template_name = "edit_task.html"
    fields = ("title", "description")


class TaskDeleteView(DeleteView):
    model = models.TodoList
    template_name = "delete_task.html"
    success_url = reverse_lazy("list_task")