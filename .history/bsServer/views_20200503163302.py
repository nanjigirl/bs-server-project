import json
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
     if request.method == "GET":
        articles = {}
        query_art = Article.objects.all()
        for title in query_art:
            articles[title.title] = title.status
        return JsonResponse({"status":"BS.200","all_titles":articles,"msg":"query articles sucess."})
