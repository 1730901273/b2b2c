from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json
# 生成JWT taken固定格式
from rest_framework_jwt.settings import api_settings

from Bills.models import bill
from Bills.serializers import getBill

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# from django.shortcuts import render


# 加入模本
# def index(request):
#     return render(request, 'index.html')


# 创建记事本API
@csrf_exempt
def getBills(request):
    """创建一个片段，实现数据交互,实现查询列表或插入数据"""
    if request.method == 'GET':
        Bills_all = bill.objects.all()
        serializer = getBill(Bills_all, many=True)
        response = HttpResponse(json.dumps({"data": serializer.data}))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    elif request.method == 'POST':
        data = request.POST.get("bill")
        action = request.POST.get("action")
        data = json.loads(data)

        if action == 'append':  # 添加数据
            serializer = bill.objects.create(**data)
            serializer.save()
            Bills_all = bill.objects.filter(amount=data['amount'], memo=data['memo'])
            ser = getBill(Bills_all, many=True)
            response = HttpResponse(json.dumps({"data": ser.data}))
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        elif action == 'remove':  # 删除数据
            bill.objects.filter(id=data['id']).delete()
            response = HttpResponse(json.dumps({"data": data}))
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        elif action == 'revamp':
            # 修改账本信息.
            Bill = bill.objects.get(id=data['id'])
            Bill.amount = data['amount']
            Bill.memo = data['memo']
            Bill.time = data['time']
            Bill.save()
            response = HttpResponse(json.dumps({"data": data}))
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        # 实现模糊匹配的API
        elif action == 'search':
            # 修改账本信息.
            value = []
            d = bill.objects.filter(memo__contains=data)
            serializer = getBill(d, many=True)
            value += serializer.data
            d = bill.objects.filter(amount__contains=data)
            serializer = getBill(d, many=True)
            value += serializer.data
            d = bill.objects.filter(time__contains=data)
            serializer = getBill(d, many=True)
            value += serializer.data
            # 去重
            new_value = []
            for data in value:
                if data not in new_value:
                    new_value.append(data)
            response = HttpResponse(json.dumps({"data": new_value}))
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        else:
            return JsonResponse(data=None, status=404)

    else:
        return JsonResponse(data=None, status=500)
