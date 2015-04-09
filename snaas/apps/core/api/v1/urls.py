from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^snorse/$', views.snorse_view, name='snorse'),
    url(r'^desnorse/$', views.desnorse_view, name='desnorse'),
)
