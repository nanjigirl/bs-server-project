from django.http import HttpResponse
import json
from bsServer.models import BookInfo

# Create your views here.


def index(request):
    # return HttpResponse('Hello World')
    list = BookInfo.objects.all()
    context = {'booklist': list}
    return HttpResponse(context)
