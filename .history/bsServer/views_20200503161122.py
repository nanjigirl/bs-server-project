from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
  # return HttpResponse('Hello World')
  list = BookInfo.objects.all()
  context = { 'booklist': '123' }
  return HttpResponse(context)