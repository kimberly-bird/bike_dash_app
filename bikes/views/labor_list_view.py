from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from bikes.models import Labor


@login_required
def labor_list(request):
    '''View for list of user's labor

        Allowed verbs: GET

        returns rendered list of all labor 
    '''
    
    if request.method == "GET":
        current_user = request.user
        labor = Labor.objects.order_by('-date').filter(user_id=current_user.id)
        context = {"labor_list": labor}
        return render(request, 'labor/list.html', context)
