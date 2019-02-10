from bikes.forms import UserForm, BikeForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
import uuid

from django.contrib.auth.models import User

from bikes.models import Bike
from bikes.models import BikeModel
from bikes.models import Brand
from bikes.models import Condition
from bikes.models import Status


@login_required
def add_bike(request):
    '''View for adding bike

    Allowed verbs: GET, POST

    returns form to post new bike and redirects users to a list of user's bikes
    '''
    if request.method == "GET":
        #render the form page
        bike_form = BikeForm()
        return render(request, 'bikes/create.html', {"bike_form": bike_form})

    if request.method == "POST":
        form_data = request.POST

        newBike = Bike(
            user = request.user,
            brand = Brand.objects.get(id=form_data['brand']),
            bikemodel = BikeModel.objects.get(id=form_data['bikemodel']),
            condition = Condition.objects.get(id=form_data['condition']),
            status = Status.objects.get(id=form_data['status']),
            created_at = datetime.date.today(),
            name = form_data['name'],
            year = form_data['year'],
            description = form_data['description'],
            purchase_price = form_data['purchase_price'],
            purchase_date = form_data['purchase_date'],
            list_price = None,
            sale_price = None,
            sale_date = None,
            document = request.FILES['document'],
        )
        newBike.save()
        messages.success(request, 'Saved!')
        return HttpResponseRedirect(reverse("bikes:bike_list"))
