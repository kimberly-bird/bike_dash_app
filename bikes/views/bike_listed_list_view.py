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
        bikes = Bike.objects.order_by('-status_id').filter(user_id=current_user.id)
        bikes_listed = Bike.objects.filter(user_id=current_user.id, status_id=2)
        all_bike_count = bikes.count()
        sold_bikes = bikes.filter(status_id=1).count()
        listed_bikes = bikes.filter(status_id=2).count()
        in_process_bikes = bikes.filter(status_id=3).count()
        context = {"bike_list": bikes_listed, "all_bike_count": all_bike_count, "sold_bikes": sold_bikes, "listed_bikes": listed_bikes, "in_process_bikes": in_process_bikes}
        return render(request, 'bikes/listed_list.html', context)
        
