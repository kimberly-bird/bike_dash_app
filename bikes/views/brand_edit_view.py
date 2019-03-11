from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from bikes.forms import BrandForm
from bikes.models import Brand


@login_required
def edit_brand(request, pk):
    '''View for editing bike brand.

    Allowed verbs: GET, POST

    returns form to edit bike brand and redirects users to a link to list of bike brands, with the list of models
    '''

    brand = get_object_or_404(Brand, pk=pk)

    if request.method == "POST":
        brand_form = BrandForm(request.POST, instance=brand)
        if brand_form.is_valid():
            brand = brand_form.save()
            return redirect('bikes:brand_list')
    else:
        brand_form = BrandForm(instance=brand)

    return render(request, 'brands/edit.html', {'brand_form': brand_form, 'pk': brand.id})