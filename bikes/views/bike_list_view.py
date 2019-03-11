from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from bikes.models import Bike


@login_required
def bike_list(request, status_id):
    '''View for list of user's bikes. This view gets a list of all user's bikes, as well as filter the bike list based on status. The template renders a sub nav component which allows users to click affordances with the status name. When the user clicks a status affordance, they are presented with a list of bikes that are filtered by status. The sub nav component also calculates the number of bikes that have that status id and shows that count on a badge. 

        Allowed verbs: GET

        returns rendered list of all bikes + bikes filtered by status
    '''
    
    if request.method == "GET":
        current_user = request.user

        # all bikes
        all_bikes = Bike.objects.order_by('-status').filter(user_id=current_user.id)
        all_bike_count = all_bikes.count()

        # bikes by in process status
        bikes_in_process = all_bikes.filter(user_id=current_user.id, status_id=3)
        in_process_bikes = bikes_in_process.count()

        # bikes by listed status
        bikes_listed = all_bikes.filter(user_id=current_user.id, status_id=2)
        listed_bikes_count = bikes_listed.count()

        # bikes by sold status
        bikes_sold = all_bikes.filter(user_id=current_user.id, status_id=1)
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
        
