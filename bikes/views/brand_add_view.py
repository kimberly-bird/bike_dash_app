from bikes.forms import UserForm, BrandForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bikes.models import Brand

@login_required
def add_brand(request):
    '''View for adding bike brands

    Allowed verbs: GET, POST

    returns form to post new bike brands and redirects users to a link to list of bike brands
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

