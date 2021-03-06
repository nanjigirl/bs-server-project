import json
import datetime
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.


def DateEncoder(obj):
    if isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')


def index(request):
    book_list = []
    # 获取所有商品
    books = BookInfo.objects.all()
    # for item in books:
    #     json_dict = {}
    #     # 获取商品的每个字段，键值对形式
    #     json_dict['id'] = item.id
    #     json_dict['title'] = item.title
    #     json_dict['pub_date'] = item.pub_date
    #     book_list.append(json_dict)

json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
    return HttpResponse(json.dumps(book_list, default=DateEncoder), content_type='application/json')
