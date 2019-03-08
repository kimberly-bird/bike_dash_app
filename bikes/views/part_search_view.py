from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from bikes.models import Part


def part_search(request):
    """Displays search results when a user searches for a bike part

    Returns:
        render -- loads the page with search results when it receives a POST. Message displayed if no results.
        HttpResponseRedirect -- if a user goes directly to the url, they are redirected to the parttype list view.
    """

    if request.method == "POST":

        search_text = request.POST["search_text"]

        if search_text is not "":
            by_make = Part.objects.filter(part_make__contains=search_text).order_by("name")
            by_model = Part.objects.filter(part_model__contains=search_text).order_by("name")
            by_name = Part.objects.filter(name__contains=search_text).order_by("name")
            results = by_make | by_model | by_name
            context = {
                "results": results,
                "length": len(results),
                "search_text": search_text,
                "no_results": True if len(results) is 0 else False
            }
        else:
            context = {
                "no_results": True,
                "search_text": search_text
            }
        return render(request, 'parts/search.html', context)

    else:
        return HttpResponseRedirect(reverse('bikes:parttype_list'))