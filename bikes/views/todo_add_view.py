from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

import datetime

from bikes.forms import ToDoForm
from bikes.models import Bike
from bikes.models import Labor
from bikes.models import ToDo


@login_required
def add_todo(request):
    '''View for adding todo.

    Allowed verbs: GET, POST

    returns form to post new bike todo and redirects users to a list of bike todo
    '''

    if request.method == "GET":
        #render the form page
        todo_form = ToDoForm(request=request)
        return render(request, 'todo/create.html', {"todo_form": todo_form})

    if request.method == "POST":
        form_data = request.POST

        newTodo = ToDo(
            user = request.user,
            bike = Bike.objects.get(id=form_data['bike']),
            notes = form_data['notes'],
            date = form_data['date'],
            title = form_data['title'],
        )

        newTodo.save()
        messages.success(request, 'Saved!')
        # after posting labor, redirect to that bike's detail page
        return HttpResponseRedirect(reverse('bikes:bike_detail', args=(newTodo.bike.id,)))


