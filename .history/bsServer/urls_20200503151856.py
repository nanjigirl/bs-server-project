from django.conf.urls import url
form views import bsServer.views
urlPatterns = [
  url('^index/$', bsServer.views.index)
]