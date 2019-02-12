from django.shortcuts import render

from bikes.models import Part
from django.contrib.auth.models import User


def part_list(request):
    '''View for list of user's parts

        Allowed verbs: GET

        returns rendered list of all parts, and displays if part is on a current bike

        TO DO: if a part is on a bike that is marked as or "Sold", then do not appear in this list (because it is on a bike that is no longer in inventory)
    '''

    if request.method == "GET":
        current_user = request.user
        parts = Part.objects.filter(user_id=current_user.id)
        context = {"part_list": parts}
        return render(request, 'parts/list.html', context)
