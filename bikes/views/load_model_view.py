from django.shortcuts import render

from bikes.models import BikeModel
from bikes.models import Brand


def load_models(request):
    brand_id = request.GET.get('brand')
    bikemodels = BikeModel.objects.filter(brand_id=brand_id).order_by('name')
    return render(request, 'bikes/bikemodel_dropdown_list_options.html', {'bikemodels': bikemodels})