from bikes.forms import BikeModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from bikes.models import Brand
from bikes.models import BikeModel


@login_required
def edit_bike_model(request, pk):
    bike_model = get_object_or_404(BikeModel, pk=pk)

    if request.method == "POST":
        bike_model_form = BikeModelForm(request.POST, instance=bike_model)
        if bike_model_form.is_valid():
            bike_model = bike_model_form.save()
            return redirect('bikes:brand_list')
    else:
        bike_model_form = BikeModelForm(instance=bike_model)

    return render(request, 'bike_models/edit.html', {'bike_model_form': bike_model_form, 'pk': bike_model.id})