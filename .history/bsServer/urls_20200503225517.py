from django.conf.urls import url
from bsServer import views

urlpatterns = [
    url('^index/$', views.index),
    url('^manager/manager', views.manager_data)
]
