from django.db import models


class TodoListItem(models.Model):
    content = models.TextField()


class SubTodoItem(models.Model):
    add_sub_title = models.ForeignKey(TodoListItem, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
