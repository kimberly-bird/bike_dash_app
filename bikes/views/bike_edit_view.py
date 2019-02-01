from bikes.forms import BikeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from bikes.models import Bike


@login_required
def edit_bike(request, pk):
    bike = get_object_or_404(Bike, pk=pk)

    if request.method == "POST":
        bike_form = BikeForm(request.POST, instance=bike)
        if bike_form.is_valid():
            bike = bike_form.save()
            return redirect('bikes:bike_list')
    else:
        bike_form = BikeForm(instance=bike)

    return render(request, 'bikes/edit.html', {'bike_form': bike_form, 'pk': bike.id})