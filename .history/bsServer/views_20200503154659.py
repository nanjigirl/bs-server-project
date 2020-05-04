from django.shortcuts import render
from django.http import HttpResponse
from bsServer.models import *
# Create your views here.
def index(request):
  # return HttpResponse('Hello World')
  BookInfo.objects.all()