from django.shortcuts import render

from bikes.models import Bike
from django.contrib.auth.models import User


def bike_list(request):
    '''View for list of user's bikes

        Allowed verbs: GET

        returns rendered list of all bikes 
    '''
    if request.method == "GET":
        current_user = request.user
        print(current_user.id)
        bikes = Bike.objects.filter(user_id=current_user.id)
        context = {"bike_list": bikes}
        return render(request, 'bikes/list.html', context)
