from django.shortcuts import render, get_object_or_404

from bikes.models import Bike
from django.contrib.auth.models import User


def bike_detail(request, pk):
    '''View for bike detail

        Allowed verbs: GET

        returns details about specific bike
    '''
    if request.method == "GET":
        current_user = request.user
        bike = get_object_or_404(Bike, pk=pk)
        context = {"bike": bike}
        return render(request, 'bikes/detail.html', context)
