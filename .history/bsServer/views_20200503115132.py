from django.shortcuts import render
from bsServer.models import BookInfo
# Create your views here.

def BookDB(request):
  list = BookInfo.objects.all()
  context = { 'booklist': list }
  return render(request, '')