import json
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    if request.method == "GET":
        list = {}
        query_book = BookInfo.objects.all()
        for title in query_book:
            list[title.title] = title.status
        return JsonResponse({"status": "BS.200", "all_titles": articles, "msg": "query articles sucess."})
