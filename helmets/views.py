from django.shortcuts import render, get_object_or_404
from . models import HelmetsM


def helmetview(request):
    all_helmets = HelmetsM.objects.all()
    return render(request, 'helmets/index.html', {'all_helmets': all_helmets})


def detail(request, helmet_id):
    helmet = get_object_or_404(HelmetsM, pk=helmet_id)
    return render(request, 'helmets/detail.html', {'helmet': helmet})
