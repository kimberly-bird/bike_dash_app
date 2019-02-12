from django.shortcuts import render

from bikes.models import Labor
from django.contrib.auth.models import User


def labor_list(request):
    '''View for list of user's labor

        Allowed verbs: GET

        returns rendered list of all labor 
    '''
    
    if request.method == "GET":
        current_user = request.user
        labor = Labor.objects.filter(user_id=current_user.id)
        context = {"labor_list": labor}
        return render(request, 'labor/list.html', context)
