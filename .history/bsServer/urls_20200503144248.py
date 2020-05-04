from django.conf.urls import url
from views import *

urlPatterns = [
  url('^index/$', views.index())
]