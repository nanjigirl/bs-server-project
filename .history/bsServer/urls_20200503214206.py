from django.conf.urls import url
from bsServer import views

urlpatterns = [
    url('^index/$', views.index)
    url('^api/ma', views.manager_data)
]
