from django.db import models


class TodoListItem(models.Model):
    content = models.TextField()


class AddsubTodoItem(models.Model):
    add_sub_title = models.ForeignKey(TodoListItem, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
