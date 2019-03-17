from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from bikes.forms import ToDoForm
from bikes.models import Bike
from bikes.models import ToDo


@login_required
def edit_todo(request, pk):
    '''View for editing bike todo.

    Allowed verbs: GET, POST

    returns form to edit bike todo and redirects users to a link to list of todos
    '''

    todo = get_object_or_404(ToDo, pk=pk)

    if request.method == "POST":
        todo_form = ToDoForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo = todo_form.save()
            return HttpResponseRedirect(reverse('bikes:bike_list', args=(4,)))
    else:
        todo_form = ToDoForm(instance=todo, request=request)

    return render(request, 'todo/edit.html', {'todo_form': todo_form, 'pk': todo.id})