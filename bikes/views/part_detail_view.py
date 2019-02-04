from django.shortcuts import render, get_object_or_404

from bikes.models import Part


def part_detail(request, pk):
    '''View for part detail

        Allowed verbs: GET

        returns details about specific part
    '''
    if request.method == "GET":
        part = get_object_or_404(Part, pk=pk)
        context = {"part": part}
        return render(request, 'parts/detail.html', context)
