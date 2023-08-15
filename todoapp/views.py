from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem, AddsubTodoItem


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, id):
    y = TodoListItem.objects.get(id=id)
    y.delete()
    return HttpResponseRedirect('/todoapp/')


def addsubTodoView(request, id):
    text = request.POST.get('subtitle')
    parent_item = TodoListItem.objects.get(id=id)
    new_item = AddsubTodoItem(add_sub_title=parent_item, content=text)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')
