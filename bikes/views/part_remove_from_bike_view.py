from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from bikes.models import Part


@login_required
def remove_part_from_bike(request, pk):
    part = get_object_or_404(Part, pk=pk)

    part.bike = None
    part.save()

    return HttpResponseRedirect(reverse("bikes:part_list"))
