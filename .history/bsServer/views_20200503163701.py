import json
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.


def index(request):
    if request.method == "GET":
        # query_book = BookInfo.objects.all()
        booklist = {'list': '123'}
    return JsonResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
