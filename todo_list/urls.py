from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("tasks/", views.TaskListView.as_view(), name="list_task"),
    path("new", views.TaskCreateView.as_view(), name="create_task"),
    path("<int:pk>/edit/", views.TaskEditView.as_view(), name="edit_task"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="delete_task"),
]