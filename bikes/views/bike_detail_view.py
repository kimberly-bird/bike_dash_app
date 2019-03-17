from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from bikes.models import Bike
from bikes.models import Labor
from bikes.models import ToDo


@login_required
def bike_detail(request, pk):
    '''View for bike detail. This view also calculates the total amount of labor spent on this bike in both hours and dollars. The rendered template also calculates total labor for each itemized labor entry, but that calculation is done in the Labor model, with an @property decorator.

        Allowed verbs: GET

        returns details about specific bike and total labor spent on the bike
    '''
    
    if request.method == "GET":
        current_user = request.user
        # get bike details
        bike = get_object_or_404(Bike, pk=pk)
        # get labor associated with specific bike
        labor = Labor.objects.order_by('-date').filter(bike_id=pk)
        # get to-dos associated with specific bike
        todo = ToDo.objects.order_by('date').filter(bike_id=pk, is_completed=False)

        # get total amount of time spent on the bike so far to display above the list of itemized labor records
        total_time = list(labor.aggregate(Sum('time')).values())[0]

        # loop over labor and calculate the $ total invested for each labor record
        total_labor = 0
        for l in labor:
            total_labor += l.time * l.rate_of_pay 
            
        context = {"bike": bike, "total_labor": total_labor, "total_time": total_time, "labor_list": labor, "todo_list": todo}
        return render(request, 'bikes/detail.html', context)
