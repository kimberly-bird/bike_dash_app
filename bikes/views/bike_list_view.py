from django.shortcuts import render

from bikes.models import Bike


def bike_list(request):
    '''View for list of user's bikes

        Allowed verbs: GET

        returns rendered list of all bikes 
    '''
    if request.method == "GET":
        bikes = Bike.objects.all()
        context = {"bike_list": bikes}
        return render(request, 'bikes/list.html', context)
