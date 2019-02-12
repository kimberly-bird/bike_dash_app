from django.shortcuts import render

from bikes.models import BikeModel
from bikes.models import Brand


def load_models(request):
    '''View to get the brand of a bike and filter the models based on the foreign key relationship. This is used whenever a user is on a form where the user can select a bike brand and only the associated bike models are available in the dropdown. There is some more functionality for this in the static index.js file.

    Allowed verbs: GET

    returns bikemodels based on selected bike brand from a dropdown
    '''

    brand_id = request.GET.get('brand')
    bikemodels = BikeModel.objects.filter(brand_id=brand_id).order_by('name')
    return render(request, 'bikes/bikemodel_dropdown_list_options.html', {'bikemodels': bikemodels})