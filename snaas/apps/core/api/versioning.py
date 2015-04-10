from rest_framework import versioning

from version import Version


class AcceptHeaderTupleVersioning(versioning.AcceptHeaderVersioning):
    def determine_version(self, request, *args, **kwargs):
        version = super(
            AcceptHeaderTupleVersioning,
            self,
        ).determine_version(request, *args, **kwargs)
        if version:
            return Version(version)
        return None
