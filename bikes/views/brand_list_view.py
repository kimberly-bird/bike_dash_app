from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from bikes.models import Brand
from bikes.models import BikeModel


@login_required
def brand_list(request):
    '''View for list of Brands 

        Allowed verbs: GET

        returns rendered list of all bike brands and associated list of bike models
    '''
    
    if request.method == "GET":
        bike_brands = Brand.objects.all().order_by('name')
        bike_models = BikeModel.objects.all()
        context = {"bike_model_list": bike_models, "bike_brand_list": bike_brands}
        return render(request, 'brands/list.html', context)
