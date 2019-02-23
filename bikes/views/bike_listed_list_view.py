from django.shortcuts import render

from bikes.models import Bike
from django.contrib.auth.models import User


def bike_listed_list(request):
    '''View for list of user's bikes

        Allowed verbs: GET

        returns rendered list of all bikes marked as sold
    '''
    
    if request.method == "GET":
        current_user = request.user
        bikes = Bike.objects.order_by('-status_id').filter(user_id=current_user.id, status_id=2)
        context = {"bike_list": bikes}
        return render(request, 'bikes/listed_list.html', context)
        
