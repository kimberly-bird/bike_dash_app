from bikes.forms import PartForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from bikes.models import Part


@login_required
def edit_part(request, pk):
    part = get_object_or_404(Part, pk=pk)

    if request.method == "POST":
        part_form = PartForm(request.POST, instance=part)
        if part_form.is_valid():
            part = part_form.save()
            return redirect('bikes:part_list')
    else:
        part_form = PartForm(instance=part)

    return render(request, 'parts/edit.html', {'part_form': part_form, 'pk': part.id})