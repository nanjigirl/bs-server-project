from django.conf.urls import url
from bsServer.views import views
urlPatterns = [
  url('^index/$', views.index)
]