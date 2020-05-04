from django.conf.urls import url
from bsServer import views

urlPatterns = [
  url('^index/$', bsServer.views.index)
]