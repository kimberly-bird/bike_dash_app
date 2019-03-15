from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from bikes.models import ToDo


@login_required
def todo_list(request):
    '''View for list of user's to do lists

        Allowed verbs: GET

        returns rendered list of all parts, and displays if part is on a current bike

        TO DO: if a part is on a bike that is marked as or "Sold", then do not appear in this list (because it is on a bike that is no longer in inventory)
    '''

    if request.method == "GET":
        current_user = request.user
        todo = ToDo.objects.order_by('date').filter(user=current_user)
        context = { "todo_list": todo }
        return render(request, 'todo/list.html', context)
