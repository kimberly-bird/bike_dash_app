from django.contrib import messages
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
        current_user = request.user
        todo.user = current_user
        todo.bike = Bike.objects.get(id=request.POST['bike'])
        todo.notes = request.POST['notes']
        todo.date = request.POST['date']
        todo.title = request.POST['title']
        todo.save()
        messages.success(request, "Edited!")
        return HttpResponseRedirect(reverse('bikes:todo_list'))
    else:
        todo_form = ToDoForm(instance=todo, request=request)

    return render(request, 'todo/edit.html', {'todo_form': todo_form, 'pk': todo.id})