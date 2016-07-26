from django.shortcuts import render, get_object_or_404
from . models import SwordsM


def swordview(request):
    all_swords = SwordsM.objects.all()
    return render(request, 'swords/index.html', {'all_swords': all_swords})


def detail(request, sword_id):
    sword = get_object_or_404(SwordsM, pk=sword_id)
    return render(request, 'swords/detail.html', {'sword': sword})
