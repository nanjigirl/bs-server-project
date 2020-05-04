import json
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.


def index(request):
    booklist = serializers.serialize("json",BookInfo.objects.all())
    return JsonResponse({"status": "200", "list": booklist, "msg": "query articles sucess."})
