from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from bikes.forms import BikeForm
from bikes.models import Bike


@login_required
def edit_bike(request, pk):
    '''View for edit bike. This view allows users to edit the main specs of the bike. It does not allow users to update the status or enter data for list price, sale price, or sale date.

    Allowed verbs: GET, POST

    returns a form to edit the bike and the posts to database
    '''
    
    bike = get_object_or_404(Bike, pk=pk)

    if request.method == "POST":
        bike_form = BikeForm(request.POST, request.FILES, instance=bike)
        if bike_form.is_valid():
            bike = bike_form.save()
            return HttpResponseRedirect(reverse('bikes:bike_detail', args=(bike.id,)))
    else:
        bike_form = BikeForm(instance=bike)

    return render(request, 'bikes/edit.html', {'bike_form': bike_form, 'pk': bike.id})