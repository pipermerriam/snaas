from django.conf.urls import patterns, include, url

from django.conf import settings

from snaas.apps.core import views


urlpatterns = patterns(
    '',
    # Site Home Page
    url(r'^$', views.SiteIndexView.as_view(), name='site-index'),

    # API
    url(r'^api/', include('snaas.apps.core.api.urls')),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
