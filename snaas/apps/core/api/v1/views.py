from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import snorse


@csrf_exempt
def snorse_view(request, *args, **kwargs):
    return HttpResponse(snorse.snorse(unicode(request.body, encoding='utf8')))


@csrf_exempt
def desnorse_view(request, *args, **kwargs):
    return HttpResponse(
        snorse.desnorse(
            unicode(request.body, encoding='utf8'),
        ),
    )
