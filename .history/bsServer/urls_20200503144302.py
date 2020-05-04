from django.conf.urls import url
import views

urlPatterns = [
  url('^index/$', views.index)
]