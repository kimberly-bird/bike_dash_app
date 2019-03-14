from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

import datetime

from bikes.forms import LaborForm
from bikes.models import Bike
from bikes.models import Labor
from bikes.models import ToDo


@login_required
def add_labor(request):
    '''View for adding bike labor. Whenever a user works on a bike, they can record some details about that work, including time and "rate of pay". The labor model has a @property decorator method that calculates the time*rate_of_pay for each labor entry.

    Allowed verbs: GET, POST

    returns form to post new bike labor and redirects users to a list of bike labor
    '''

    if request.method == "GET":
        #render the form page
        labor_form = LaborForm(request)
        return render(request, 'labor/create.html', {"labor_form": labor_form})

    if request.method == "POST":
        form_data = request.POST

        newLabor = Labor(
            user = request.user,
            bike = Bike.objects.get(id=form_data['bike']),
            notes = form_data['notes'],
            date = datetime.date.today(),
            time = form_data['time'],
            rate_of_pay = form_data['rate_of_pay'],
            todo = ToDo.objects.get(id=form_data['todo']),
        )

        newLabor.save()
        messages.success(request, 'Saved!')
        # after posting labor, redirect to that bike's detail page
        return HttpResponseRedirect(reverse('bikes:bike_detail', args=(newLabor.bike.id,)))


