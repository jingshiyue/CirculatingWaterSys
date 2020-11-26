from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
# from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .serializers import *
from . import models
from .models import Device
from .permissions import AdminPermission
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from utils.utils import sqlFetchone,sqlFetchall
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework_jwt.utils import jwt_decode_handler
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)
# Create your views here.
class Pagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 10

# CacheResponseMixin list和retrieve 才会缓存,需要后台配置
class DeviceEditViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,AdminPermission]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = DeviceSerializer
    lookup_field = "device_id"

    def get_queryset(self):
        return Device.objects.all()

class DeviceQueryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = DeviceSerializer
    lookup_field = "device_id"

    def get_queryset(self):
        return Device.objects.all().order_by("-create_time")


class QueryStatisticsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        dataDict = {}
        total = sqlFetchone("select count(1) from device_device")
        dataDict.setdefault("total",total[0])
        online = sqlFetchone("select count(1) from device_device where online=1")
        dataDict.setdefault("online",online[0])
        dataDict.setdefault("fault",0)
        return JsonResponse(dataDict)

class QueryDeviceAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request):
        dateGet = (request.GET) #{"DeviceID": "zhuban", "NetState": "0", "DeviceState": "11"}
        MainboardID = dateGet.get("MainboardID",None)
        online = dateGet.get("NetState",None)
        dev_state = dateGet.get("DeviceState",None)
        conditions ={
            "MainboardID":MainboardID,
            "online":online,
            "dev_state":dev_state
        }
        obj = models.Device.objects.filter(**conditions)
        serislizer=DeviceSerializer(instance=obj,many=True,)
        return JsonResponse(serislizer.data,safe=False)
        # return HttpResponse(obj)


class RepairDeviceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,AdminPermission]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = RepairDeviceSerializer
    lookup_field = "repairID"
    pagination_class = Pagination

    def get_queryset(self):
        return RepairDevice.objects.all().order_by("-create_time")

    def create(self, request, *args, **kwargs):
        deviceNum = request.data.get("deviceNum")
        # n = models.RepairDevice.objects.filter(deviceNum=" 1021").count()
        sql = f"SELECT count(*) FROM `device_repairdevice` WHERE deviceNum= {deviceNum}"
        n = sqlFetchone(sql)[0]
        repairID = deviceNum + "-" + str(n+1)
        queryDict = request.data.copy()
        queryDict.setdefault("repairID",repairID)
        serializer = self.get_serializer(data=queryDict)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED,)

    def perform_create(self, serializer):
        serializer.save()


class AddFeedbackAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request,repairID):
        return render(request,'device/index/repairs/addfeedback.html')

    def put(self,request,repairID):
        obj = RepairDevice.objects.get(repairID=repairID)
        validated_data = RepairDeviceSerializer(instance=obj,data=request.data,partial=True)
        if validated_data.is_valid():
            validated_data.save()
            return Response(validated_data.data)
        else:
            return Response(validated_data.errors)



class AfterSaleManageViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,AdminPermission]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = AfterSaleManageSerializer
    lookup_field = "id"
    pagination_class = Pagination

    def get_queryset(self):
        return AfterSaleManage.objects.all()


class AddAfterSaleAPIView(APIView):
     def get(self, request):
        dateGet = request.GET
        logger.debug(dateGet) 
        logger.debug(id)
        return render(request,'device/index/remind/add.html')
        

# def get_user(request):
#     from rest_framework_jwt.authentication import JSONWebTokenAuthentication 
#     from rest_framework.views import exception_handler
#     from rest_framework_jwt.utils import jwt_decode_handler
#     # 获取登陆的用户
#     token = request.META.get('HTTP_AUTHORIZATION')[4:]
#     logger.debug(token)
#     token_user = jwt_decode_handler(token)

#     user_id = token_user['user_id']  # 获取用户id
#     # sql = f"SELECT username FROM `auth_user` WHERE id= {user_id}"
#     # username = sqlFetchone(sql)[0]
#     return HttpResponse(user_id)

class ChangePwdAPIView(APIView):

    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request):
        return render(request,'device/index/user/changePwd.html')

    def post(self,request):
        # 获取登陆的用户
        request_data = request.data
        # return JsonResponse({"msg":"密码更改成功"})

        cookies = request.COOKIES
        token_user = jwt_decode_handler(cookies["token"])
        user_id = token_user['user_id']  # 获取用户id
        user = User.objects.get(id=user_id)
        old_password = request_data.get("password_old")
        new_password = request_data.get("password_new")
        re_password_new = request_data.get("re_password_new")
        if new_password != re_password_new:
            logger.debug({"msg":"重设的两次密码输入不一致"})
            return JsonResponse({"msg":"重设的两次密码输入不一致"})
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            logger.debug({"msg":"密码更改成功"})
            return JsonResponse({"msg":"密码更改成功"})
        logger.debug({"msg":"输入的原始密码不正确"})
        return JsonResponse({"msg":"输入的原始密码不正确"})


class ParamSetAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request,device_id):
        return render(request,'device/index/setting/sell/Id/paramSet.html')

    def put(self,request,device_id):
        obj = Device.objects.get(device_id=device_id)
        validated_data = DeviceSerializer(instance=obj,data=request.data,partial=True)
        if validated_data.is_valid():
            validated_data.save()
            return Response(validated_data.data)
        else:
            return Response(validated_data.errors)

class ModifyAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request,device_id):
        return render(request,'device/index/Equipment/edit/Id/modify.html')
    def put(self,request,device_id):
        obj = Device.objects.get(device_id=device_id)
        validated_data = DeviceSerializer(instance=obj,data=request.data,partial=True)
        if validated_data.is_valid():
            validated_data.save()
            return Response(validated_data.data)
        else:
            return Response(validated_data.errors)

class moreAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request,device_id):
        return render(request,'device/index/Equipment/info/Id/more.html')

class RunStatusAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request,device_id):
        return render(request,'device/index/Equipment/statetu/Id/runStatus.html')

    def put(self,request,device_id):
        obj = Device.objects.get(device_id=device_id)
        validated_data = DeviceSerializer(instance=obj,data=request.data,partial=True)
        if validated_data.is_valid():
            validated_data.save()
            return Response(validated_data.data)
        else:
            return Response(validated_data.errors)



            