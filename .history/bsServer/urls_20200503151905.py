from django.conf.urls import url
from views import bsServer.views
urlPatterns = [
  url('^index/$', views.index)
]