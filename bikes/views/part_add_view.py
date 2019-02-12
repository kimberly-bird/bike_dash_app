from bikes.forms import UserForm, PartForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

from bikes.models import Bike
from bikes.models import BikeModel
from bikes.models import Brand
from bikes.models import Part
from bikes.models import PartType


@login_required
def add_part(request):
    '''View for adding bike parts. Bike parts sometimes have a specific bike brand and model, but other times, they are not associated with a specific bike manufacturer and have their own make/models. The user is not required to select both a bike brand/model AND part_make/part_model - it's likely that they will only fill out one pair. For example, a bike frame will have a bike manufactured brand/model, whereas a bike chain will not and will have its own make/model that the user can manually enter.

    Allowed verbs: GET, POST

    returns form to post new bike parts and redirects users to a list of bike parts
    '''

    if request.method == "GET":
        #render the form page
        part_form = PartForm()
        return render(request, 'parts/create.html', {"part_form": part_form})

    if request.method == "POST":
        form_data = request.POST

        newPart = Part(
            user = request.user,
            bike = form_data.get(Bike, None),
            brand = form_data.get(Brand, None),
            bikemodel = form_data.get(BikeModel, None),
            parttype = PartType.objects.get(id=form_data['parttype']),
            name = form_data['name'],
            part_make = form_data['part_make'],
            part_model = form_data['part_model'],
            created_at = datetime.date.today(),
            notes = form_data['notes'],
            purchase_price = form_data['purchase_price'],
            document = request.FILES['document'],
        )

        newPart.save()
        messages.success(request, 'Saved!')
        return HttpResponseRedirect(reverse("bikes:part_list"))

