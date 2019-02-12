from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from bikes.models import Part


@login_required
def remove_part_from_bike(request, pk):
    '''Method to remove the part from a bike from the bike detail page. On the bike detail page, the parts that are currently on the bike are listed. The user can easily click the "remove this part from the bike" affordance, which will simply remove the bike foreign key on the part, essentially putting the part back into inventory for a future bike.

    TO DO: add a confirmation "are you sure you want to remove this part from the bike?"

    Allowed verbs: GET, POST

    returns to list of parts
    '''

    part = get_object_or_404(Part, pk=pk)

    part.bike = None
    part.save()

    return HttpResponseRedirect(reverse("bikes:part_list"))
