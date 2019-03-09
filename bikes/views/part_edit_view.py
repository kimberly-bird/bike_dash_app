from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse

from bikes.forms import PartForm
from bikes.models import Part


@login_required
def edit_part(request, pk):
    '''View for editing a bike part. One key feature here is that a user can either "remove" the part from the bike or "add" the part to the bike. For example, you might have a bike chain that does not have a bike foreign key. That means the chain is simply in inventory and is available to add to a bike. Once a user is ready to take the chain from their inventory and add it to a specific bike, the user can edit the bike part and select the bike. This will then add a foreign key relationship to that part and bike.

    Allowed verbs: GET, POST

    returns form and posts update to Part
    '''

    part = get_object_or_404(Part, pk=pk)

    if request.method == "POST":
        part_form = PartForm(request.POST, request.FILES, instance=part)
        if part_form.is_valid():
            part = part_form.save()
            redirect_url = reverse('bikes:part_detail', args=[part.id])
            return HttpResponseRedirect(redirect_url)
    else:
        part_form = PartForm(instance=part)

    return render(request, 'parts/edit.html', {'part_form': part_form, 'pk': part.id})