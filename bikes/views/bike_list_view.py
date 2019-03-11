from django.shortcuts import render

from bikes.models import Bike
from django.contrib.auth.models import User


def bike_list(request, status_id):
    '''View for list of user's bikes

        Allowed verbs: GET

        returns rendered list of all bikes 
    '''
    
    if request.method == "GET":
        current_user = request.user

        # all bikes
        all_bikes = Bike.objects.order_by('-status').filter(user_id=current_user.id)
        all_bike_count = all_bikes.count()

        # bikes by in process status
        bikes_in_process = all_bikes.filter(status_id=3)
        in_process_bikes = bikes_in_process.count()

        # bikes by listed status
        bikes_listed = all_bikes.filter(status_id=2)
        listed_bikes_count = bikes_listed.count()

        # bikes by sold status
        bikes_sold = all_bikes.filter(status_id=1)
        sold_bikes_count = bikes_sold.count()

        context = {
            "bike_list": all_bikes, 
            "all_bike_count": all_bike_count, 
            "bikes_in_process": bikes_in_process,
            "in_process_bikes_count": in_process_bikes, 
            "bikes_listed": bikes_listed,
            "listed_bikes_count": listed_bikes_count, 
            "sold_bikes_count": sold_bikes_count, 
            "bikes_sold": bikes_sold,
            }
        return render(request, 'bikes/list.html', context)
        
