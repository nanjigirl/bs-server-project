import json
from django.http import HttpResponse,JsonResponse
from bsServer import models

# Create your views here.


def index(request):
    book = models.BookInfo.objects.all()
    booklist = Context({"status": "200", "list": book, "msg": "query articles sucess."})
    return HttpResponse(c)
