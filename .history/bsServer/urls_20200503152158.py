from django.conf.urls import url
import bsServer.views

urlPatterns = [
  url('^index/$', bsServer.views.index)
]