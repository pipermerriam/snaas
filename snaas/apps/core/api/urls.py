from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    # API
    url(r'^', include('snaas.apps.core.api.v1.urls')),
)
