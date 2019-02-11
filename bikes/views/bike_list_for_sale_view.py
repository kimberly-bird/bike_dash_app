from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from bikes.models import Bike
from bikes.models import Status


@login_required
def list_bike_for_sale(request, pk):
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