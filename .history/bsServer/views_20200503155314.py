from django.shortcuts import render
from django.http import HttpResponse
from bsServer.models import BookInfo

# Create your views here.
def index(request):
  # return HttpResponse('Hello World')
  bootk = BookInfo.objects.all()