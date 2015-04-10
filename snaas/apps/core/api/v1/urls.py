from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^snorse/$', views.SnorseView.as_view(), name='snorse'),
    url(r'^desnorse/$', views.DesnorseView.as_view(), name='desnorse'),
)
