from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^/snorse/$', views.SnorseAPIView.as_view(), name='snorse'),
    url(r'^/de-snorse/$', views.DeSnorseAPIView.as_view(), name='desnorse'),
)
