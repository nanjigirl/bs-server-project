import json
from django.http import HttpResponse
from bsServer import models

# Create your views here.


def index(request):
    booklist = models.BookInfo.objects.all()
    print(booklist)
    return HttpResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
