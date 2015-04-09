from rest_framework import views
from rest_framework import response

import snorse


class SnorseAPIView(views.APIView):
    def post(self, *args, **kwargs):
        return response.Response(snorse.snorse(self.request.stream.body))


class DeSnorseAPIView(views.APIView):
    def post(self, *args, **kwargs):
        return response.Response(
            snorse.desnorse(
                unicode(self.request.stream.body, encoding='utf8'),
            ),
        )
