import json
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.


def index(request):
    if request.method == "GET":
      try
        booklist = BookInfo.objects.all()
      catch {
        booklist = []
      }
    return JsonResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
