from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from bikes.models import Bike
from bikes.models import Status


@login_required
def sell_bike(request, pk):
    '''View for marking a bike as sold. When a user is on the bike detail page and the bike status is "Listed", then the user can click on a "mark this bike sold" affordance that redirects to this view. This renders a simple form that allows users to put the price they sold the bike and the date the bike was sold. On POST, the bike is updated with the price, date, and status is changed from "Listed" to "Sold"

    Allowed verbs: GET, POST

    returns form with 2 fields and posts update to Bike
    '''

    # get selected bike
    bike = get_object_or_404(Bike, pk=pk)
    status = get_object_or_404(Status, pk=1)

    if request.method == "POST":
        bike.sale_price = request.POST["sale_price"]
        bike.sale_date = request.POST["sale_date"]
        bike.status = status
        bike.save()
        return HttpResponseRedirect(reverse("bikes:bike_detail", args=(pk,)))
    else:
      context = {"bike": bike}
      return render(request, 'bikes/sell.html', context)