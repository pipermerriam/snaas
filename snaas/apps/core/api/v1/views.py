from rest_framework import views
from rest_framework import exceptions
from rest_framework.response import Response

from version import Version

import snorse


class BaseSnorsingView(views.APIView):
    version = Version("1.0.0")

    @staticmethod
    def version_acceptable(satisfied_version, requested_version):
        if satisfied_version is None or requested_version is None:
            return True
        return (
            satisfied_version.major == requested_version.major
            and requested_version <= satisfied_version
        )

    def initial(self, request, *args, **kwargs):
        ret = super(BaseSnorsingView, self).initial(request, *args, **kwargs)
        if not self.version_acceptable(self.version, request.version):
            raise exceptions.NotAcceptable
        return ret


class SnorseView(BaseSnorsingView):
    def post(self, request):
        return Response(snorse.snorse(unicode(request.body, encoding='utf8')))


class DesnorseView(BaseSnorsingView):
    def post(self, request):
        return Response(
            snorse.desnorse(
                unicode(request.body, encoding='utf8'),
            ),
        )
