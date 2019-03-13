from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from bikes.models import Bike
from bikes.models import Labor
from bikes.models import Part
from bikes.models import Status


@login_required
def list_bike_for_sale(request, pk):
    '''View for listing a bike for sale. When a user is on the bike detail page and the bike status is "In Process", then the user can click on a "list this bike for sale" affordance that redirects to this view. This renders a simple form that allows users to put the price they are listing the bike for sale. On POST, the bike is updated with the price from user input and status is changed from "In Process" to "Listed"

    Allowed verbs: GET, POST

    returns form with one field and posts update to Bike
    '''

    # get selected bike
    bike = get_object_or_404(Bike, pk=pk)
    status = get_object_or_404(Status, pk=2)

    if request.method == "POST":
        bike.list_price = request.POST["list_price"]
        bike.status = status
        bike.save()
        return HttpResponseRedirect(reverse("bikes:bike_detail", args=(pk,)))
    else:
        # get all labor for bike
        labor_list = Labor.objects.filter(bike_id=bike.id)

        # total_labor will hold the total amount of labor spent on this bike ($ value)
        total_labor = 0
        for labor in labor_list:
            # get_total_for_each_labor is a property method on the Labor model that calculates rate_of_pay*time
            labor_calculation = labor.get_total_for_each_labor
            total_labor += labor_calculation

        # get sum of purchase price for all parts for bike
        part_sum = Part.objects.filter(bike_id=bike.id).aggregate(sum=Sum('purchase_price'))

        # calculate $ amount needed to break even on bike investment 
        break_even_price = bike.purchase_price + total_labor + part_sum["sum"]

        context = {"bike": bike, "total_labor": total_labor, "part_sum": part_sum["sum"], "break_even_price": break_even_price}
        return render(request, 'bikes/list_bike.html', context)