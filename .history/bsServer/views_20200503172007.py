import json
from django.http import HttpResponse,JsonResponse
from bsServer import models

# Create your views here.


def index(request):
    booklist = models.BookInfo.objects.all()
    Context({"people_list":people_list})
    return JsonResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
