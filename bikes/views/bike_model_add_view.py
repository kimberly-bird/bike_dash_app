from bikes.forms import BikeModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bikes.models import Brand
from bikes.models import BikeModel

@login_required
def add_bike_model(request, pk):
    '''View for adding bike model for a bike brand. Each bike brand/manufacturer has many bike models, so this creates a connection between the model and the brand. In a perfect world, this data would not be user generated, but I didn't want to scrape data off a website. Any user can add a brand or bike model. TO DO: check to make sure that duplicate bike model can't be added.

    Allowed verbs: GET, POST

    returns form to post new bike models and redirects users to a link to list of bike brands, with the list of models
    '''

    if request.method == "GET":
        bike_model_form = BikeModelForm()
        brand = get_object_or_404(Brand, pk=pk)
        return render(request, 'bike_models/create.html', {"bike_model_form": bike_model_form, "brand_id": pk, "brand": brand})

    if request.method == "POST":
        newModel = BikeModel(
            name = request.POST['name'],
            brand_id = pk
        )
        newModel.save()

        messages.success(request, 'Saved!')
        return HttpResponseRedirect(reverse("bikes:brand_list"))

