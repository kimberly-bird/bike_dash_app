from django.shortcuts import render

from bikes.models import Part
from django.contrib.auth.models import User


def part_list(request):
    '''View for list of user's bikes

        Allowed verbs: GET

        returns rendered list of all bikes 
    '''
    if request.method == "GET":
        current_user = request.user
        parts = Part.objects.filter(user_id=current_user.id)
        context = {"bike_list": parts}
        return render(request, 'bikes/list.html', context)
