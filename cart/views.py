from django.http import HttpResponse
from django.template import loader


def cartview(request):
    template = loader.get_template('cart/index.html')
    return HttpResponse(template.render(request))
