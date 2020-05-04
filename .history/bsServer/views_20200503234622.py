import json
import datetime
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
    for item in books:
        json_dict = {}
        # 获取商品的每个字段，键值对形式
        json_dict['id'] = item.id
        json_dict['title'] = item.title
        json_dict['pub_date'] = item.pub_date
        book_list.append(json_dict)

    # 返回json，一定要指定类型content_type='application/json'
    return HttpResponse(json.dumps({'list': book_list, 'msg': 'success', 'status': 200}, default=DateEncoder), content_type='application/json')


def manager_data(request):
    x_list = []
    y_list = []
    # 获取所有商品
    # data = PotentialInfo.objects.all()
    x_list = PotentialInfo.objects.order_by('lastTime')
    y_list = PotentialInfo.objects.get().ProtectionPotential
    # for item in data:
    #     # 获取商品的每个字段，键值对形式
    #     x_list.append(item.lastTime)
    #     y_list.append(item.ProtectionPotential)
    manager_list = {
        'xData': x_list,
        'yData': y_list
    }
    # 返回json，一定要指定类型content_type='application/json'
    return HttpResponse(json.dumps(manager_list, default=DateEncoder), content_type='application/json')
