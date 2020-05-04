import json
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.


def index(request):
    bookList = []
    # 获取所有商品
    books = BookInfo.objects.all()
    for item in books:
        json_dict = {}
        # 获取商品的每个字段，键值对形式
        json_dict['id'] = good.name
        json_dict['title'] = good.title
        json_dict['pub_date'] = good.pub_date
        json_list.append(json_dict)

    # 返回json，一定要指定类型content_type='application/json'
    return HttpResponse(json.dumps(json_list), content_type='application/json'))
