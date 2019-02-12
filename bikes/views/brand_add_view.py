from bikes.forms import UserForm, BrandForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bikes.models import Brand

@login_required
def add_brand(request):
    '''View for adding bike brand. In a perfect world, this data would not be user generated, but I didn't want to scrape data off a website. Any user can add a brand or bike model. TO DO: check to make sure that duplicate bike brand can't be added.

    Allowed verbs: GET, POST

    returns form to post new bike brands and redirects users to a link to list of bike brands, with the list of models
    '''

    if request.method == "GET":
        #render the form page
        brand_form = BrandForm()
        return render(request, 'brands/create.html', {"brand_form": brand_form})

    if request.method == "POST":
        form_data = request.POST

        newBrand = Brand(
            name = form_data['name'],
            location = form_data['location'],
        )
        newBrand.save()
        messages.success(request, 'Saved!')
        return HttpResponseRedirect(reverse("bikes:brand_list"))

