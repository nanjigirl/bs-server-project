import json
from django.http import HttpResponse,JsonResponse
from bsServer.models import mod

# Create your views here.


def index(request):
    booklist = BookInfo.objects.all()
    print(booklist)
    return JsonResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
