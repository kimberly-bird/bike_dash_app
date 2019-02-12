from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from bikes.models import Bike
from bikes.models import Status


@login_required
def list_bike_for_sale(request, pk):
    '''View for listing a bike for sale. When a user is on the bike detail page and the bike status is "In Process", then the user can click on a "list this bike for sale" affordance that redirects to this view. This renders a simple form that allows users to put the price they are listing the bike for sale. On POST, the bike is updated with the price and status is changed from "In Process" to "Listed"

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
      context = {"bike": bike}
      return render(request, 'bikes/list_bike.html', context)