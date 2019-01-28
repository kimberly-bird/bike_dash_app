from django.shortcuts import render

from bikes.models import Brand


def brand_list(request):
    '''View for Brands of bikes page

        Allowed verbs: GET

        returns rendered list of all bike brands and lists associated bike models
    '''

    if request.method == "GET":
        brands = Brand.objects.all().order_by('name')
        context = {"brand_list": brands}
        print("context", context)
        return render(request, 'bikes/brands/list.html', context)
