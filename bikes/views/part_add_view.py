from bikes.forms import UserForm, PartForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

from bikes.models import Part


@login_required
def add_part(request):
    '''View for adding bike parts

    Allowed verbs: GET, POST

    returns form to post new bike parts and redirects users to a link to list of bike parts
    '''
    if request.method == "GET":
        #render the form page
        part_form = PartForm()
        return render(request, 'parts/create.html', {"part_form": part_form})

    if request.method == "POST":
        form_data = request.POST

        newPart = Part(
            user = request.user,
            bike = form_data['bike'],
            brand = form_data['brand'],
            bikemodel = form_data['bikemodel'],
            parttype = form_data['parttype'],
            name = form_data['name'],
            part_make = form_data['part_make'],
            part_model = form_data['part_model'],
            created_at = datetime.date.today(),
            notes = form_data['notes'],
            purchase_price = form_data['purchase_price'],
        )
        newPart.save()
        messages.success(request, 'Saved!')
        return HttpResponseRedirect(reverse("bikes:part_list"))

