from django.conf.urls import url
import bsSer
urlPatterns = [
  url('^index/$', bsServer.views.index)
]