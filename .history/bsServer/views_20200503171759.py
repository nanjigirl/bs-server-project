import json
from django.http import HttpResponse,JsonResponse
from bsServer import models

# Create your views here.


def index(request):
    booklist = BookInfo.objects.all()
    print(booklist)
    return JsonResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
