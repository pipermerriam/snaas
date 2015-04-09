from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^snorse/$', views.snorse_view, name='snorse'),
    url(r'^de-snorse/$', views.desnorse_view, name='desnorse'),
)
