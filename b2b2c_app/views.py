from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ratelimit
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from b2b2c_app.models import TbProduct, TbBuyer, bill
from b2b2c_app.serializers import product, user, getBill
from django.core.exceptions import ObjectDoesNotExist
# 生成JWT taken固定格式
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


#
#
# # Create your views here.
# # 创建一个API实现查找用户收藏表
# @csrf_exempt
# def user_fav(request):
#     """列出所有的片段，或者创建一个新的片段"""
#     if request.method == 'GET':
#         User_fav = Userfav.objects.all()
#         serializer = userfav_serializer(User_fav, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = userfav_serializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# # 写一个视图对应其models中的表，实现对它的删，改，查
# @csrf_exempt
# def userfav_detail(request, pk=2):
#     """增加，更新，删除一个数据"""
#     global user_fav
#
#     try:
#         user_fav = Userfav.objects.get(shopping_id=pk)  # 得到对应表中的对应数据
#     except ObjectDoesNotExist:
#         return HttpResponse(status=404)
#     # 更新一条数据，对应get方式访问
#     if request.method == 'GET':
#         serializer = userfav_serializer(user_fav)
#         return JsonResponse(serializer.data)
#     # 增加一条数据，对应put方式访问
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = userfav_serializer(user_fav, data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     # 删除表中一条数据，对应delete方式访问
#     elif request.method == 'DELETE':
#         user_fav.delete()
#         return HttpResponse(status=204)
#
#
# # 创建商品表的API
@csrf_exempt
def tb_product(request):
    """创建一个片段，实现数据交互,实现查询列表或插入数据"""
    if request.method == 'GET':
        tb_product_all = TbProduct.objects.all()
        serializer = product(tb_product_all, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        print(request)
        serializer = TbProduct(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data, status=201, safe=False)
        else:
            return JsonResponse(serializer.errors, status=400, safe=False)
    else:
        return JsonResponse(data=None, status=500)


# 创建登录信息的API
@csrf_exempt
# @ratelimit(key='ip', rate='5/30s', block=True)
def buyer_login(request):
    dic = {}
    if request.method == 'POST':  # 当提交表单时

        # 判断是否传参
        if request.POST:
            b_username = request.POST.get('username', 0)
            b_password = request.POST.get('password', 0)
            # 判断参数中是否含有a和b
            if TbBuyer.objects.filter(username=b_username, password=b_password):
                global tbBuyer
                try:
                    tbBuyer = TbBuyer.objects.get(username=b_username)  # 得到对应表中的对应数据
                except ObjectDoesNotExist:
                    return HttpResponse(status=404)
                serializer = user(tbBuyer)
                # 生成taken值
                payload = jwt_payload_handler(tbBuyer)
                taken = jwt_encode_handler(payload)
                tbBuyer.b_taken = taken
                tbBuyer.save()
                data = json.dumps(serializer.data)
                dic['code'] = 200
                dic['result'] = u"登录成功"
                dic['taken'] = taken
                dic['data'] = data
                return JsonResponse(dic, status=200)
            else:
                dic['code'] = 201
                dic['result'] = u"登录失败"
                dic['data'] = "账号或密码错误！"
                return JsonResponse(dic, status=304)
    else:
        dic['code'] = 500
        dic['result'] = u"登录失败"
        dic['data'] = u"方法错误"
        return JsonResponse(dic, status=500)


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

        if action == 'append':      # 添加数据
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
        elif action == 'remove':      # 删除数据
            b = bill.objects.filter(id=data['id']).delete()
            response = HttpResponse(json.dumps({"data": data}))
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        elif action == 'revamp':
            # 修改账本信息.
            print(data)
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

    else:
        return JsonResponse(data=None, status=500)
