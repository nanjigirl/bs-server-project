from django.conf.urls import url
from bsServer import views

urlPatterns = [
  url('^index/$', views.index)
]