import json
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.


def index(request):
    try:
        booklist = [{'id':1, 'title': '123', 'date': '2019-2-3'}]
    finally:
        booklist = [{'id':2, 'title': '456', 'date': '2019-2-3'}]
    return JsonResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
