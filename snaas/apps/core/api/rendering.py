from rest_framework import renderers


class SnaasVersionedText(renderers.BaseRenderer):
    media_type = 'application/vnd.snorse+txt'
    format = 'txt'

    def render(self, data, media_type=None, renderer_context=None):
        return unicode(data).encode(self.charset)
