from django.shortcuts import render, get_object_or_404
from . models import ArmorM


def armorview(request):
    all_armors = ArmorM.objects.all()
    return render(request, 'armor/index.html', {'all_armors': all_armors})


def detail(request, armor_id):
    armor = get_object_or_404(ArmorM, pk=armor_id)
    return render(request, 'armor/detail.html', {'armor': armor})


