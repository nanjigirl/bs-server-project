import json
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.


def index(request):
    try:
        booklist = BookInfo.objects.all()
    finally:
        booklist = ['id': 2, '']
    return JsonResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
