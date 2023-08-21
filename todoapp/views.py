from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem, SubTodoItem


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})


def addTodoView(request):
    text = request.POST['content']
    new_item = TodoListItem(content=text)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, id):
    item_delete = TodoListItem.objects.get(id=id)
    item_delete.delete()
    return HttpResponseRedirect('/todoapp/')


def addsubTodoView(request, id):
    text = request.POST.get('subtitle')
    parent_item = TodoListItem.objects.get(id=id)
    new_item = SubTodoItem(add_sub_title=parent_item, content=text)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')
