from django.http import HttpResponse
from bsServer.models import BookInfo
import json

# Create your views here.


def index(request):
    # return HttpResponse('Hello World')
    list = BookInfo.objects.all()
    context = {'booklist': list}
    return HttpResponse(context)