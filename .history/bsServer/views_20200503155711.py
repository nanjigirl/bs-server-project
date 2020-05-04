from django.shortcuts import render
from django.http import HttpResponse
from bsServer.models import BookInfo

# Create your views here.
def index(request):
  # return HttpResponse('Hello World')
  list = BookInfo.objects.all()
  content = { 'booklist': list }
  return render(request, request: HttpResponse('戏说不是胡说'))