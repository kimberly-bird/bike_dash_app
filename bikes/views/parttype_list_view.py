from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from bikes.models import Part
from bikes.models import PartType


@login_required
def parttype_list(request, pk):
    '''View for list of user's parts grouped by parttype

        Allowed verbs: GET

        returns rendered list of all parts, and displays if part is on a current bike

        TO DO: if a part is on a bike that is marked as or "Sold", then do not appear in this list (because it is on a bike that is no longer in inventory)
    '''

    if request.method == "GET":
        current_user = request.user
        parttype = get_object_or_404(PartType, pk=pk)
        parts = parttype.part_set.order_by('name').filter(user_id=current_user.id)
        context = {"part_list": parts, "parttype": parttype}
        return render(request, 'parts/ptlist.html', context)
