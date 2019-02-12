from bikes.forms import LaborForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

from bikes.models import Bike
from bikes.models import Labor


@login_required
def add_labor(request):
    '''View for adding bike labor

    Allowed verbs: GET, POST

    returns form to post new bike labor and redirects users to a link to list of bike labor
    '''
    if request.method == "GET":
        #render the form page
        labor_form = LaborForm()
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
        )

        newLabor.save()
        messages.success(request, 'Saved!')
        return HttpResponseRedirect(reverse("bikes:labor_list"))

