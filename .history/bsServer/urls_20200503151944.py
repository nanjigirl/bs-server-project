from django.conf.urls import url
from views import .views
urlPatterns = [
  url('^index/$', views.index)
]