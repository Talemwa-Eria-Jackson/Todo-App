from django.db import models
from django.urls import reverse

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.title}"

    def get_absolute_url(self):
        return reverse("list_task")