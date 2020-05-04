import json
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    # list = BookInfo.objects.all()
    # context = {'booklist': list}
    return HttpResponse(json.dumps(context))
