from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from bikes.models import ToDo


@login_required
def delete_todo(request, pk):
    '''View for deleting bike todo.

    Allowed verbs: DELETE

    returns user to a list of to-dos with respective to do deleted from database
    '''

    todo = get_object_or_404(ToDo, pk=pk)

    todo.delete()

    return HttpResponseRedirect(reverse('bikes:todo_list'))