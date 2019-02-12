from django.shortcuts import render, get_object_or_404
from django.db.models import Sum

from bikes.models import Bike
from bikes.models import Labor
from django.contrib.auth.models import User


def bike_detail(request, pk):
    '''View for bike detail

        Allowed verbs: GET

        returns details about specific bike
    '''
    if request.method == "GET":
        current_user = request.user
        bike = get_object_or_404(Bike, pk=pk)
        labor = Labor.objects.filter(bike_id=pk)

        total_time = list(labor.aggregate(Sum('time')).values())[0]

        total_labor = 0
        for l in labor:
            total_labor += l.time * l.rate_of_pay 
            
        context = {"bike": bike, "total_labor": total_labor, "total_time": total_time}
        return render(request, 'bikes/detail.html', context)
