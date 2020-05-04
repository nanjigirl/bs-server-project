import json
from django.shortcuts import HttpResponse, render
from .models import *

# Create your views here.


def index(request):
    booklist = BookInfo.objects.all()
    return render('request','index.html',{"status": "200", "list": booklist, "msg": "query articles sucess."})
