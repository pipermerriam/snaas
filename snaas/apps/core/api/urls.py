from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    # API
    url(r'^v1/', include('snaas.apps.core.api.v1.urls', namespace='v1')),
)
