from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from bikes.models import Bike


@login_required
def bike_search(request):
    """Displays search results when a user searches for a bike

    Returns:
        render -- loads the page with search results when it receives a POST. Message displayed if no results.
        HttpResponseRedirect -- if a user goes directly to the url, they are redirected to the bike list view.
    """

    if request.method == "POST":

        search_text = request.POST["search_text"]
        print("search text", search_text)

        if search_text is not "":
            by_name = Bike.objects.filter(name__contains=search_text).order_by("name")
            by_description = Bike.objects.filter(description__contains=search_text).order_by("name")
            by_brand = Bike.objects.filter(brand__name__contains=search_text).order_by("name")
            by_model = Bike.objects.filter(bikemodel__name__contains=search_text).order_by("name")
            results = by_name | by_description | by_brand | by_model
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
        return render(request, 'bikes/search.html', context)

    else:
        return HttpResponseRedirect(reverse('bikes:bike_list', args=(4,)))