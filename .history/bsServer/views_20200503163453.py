import json
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.


def index(request):
    if request.method == "GET":
        booklist = {}
        query_book = BookInfo.objects.all()
        for item in query_book:
            booklist[item.title] = item.status
        return JsonResponse({"status": "200", "all_titles": booklist, "msg": "query articles sucess."})
