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
import logging
from rest_framework.views import APIView
from utils.utils import sqlFetchone,sqlFetchall


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
    pagination_class = Pagination
    # permission_classes = [IsAuthenticated,AdminPermission]
    # authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = DeviceSerializer
    lookup_field = "device_id"

    def get_queryset(self):
        return Device.objects.all()

class DeviceQueryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    pagination_class = Pagination
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = DeviceSerializer
    lookup_field = "device_id"

    def get_queryset(self):
        return Device.objects.all()

def queryModulars(request):
    logger.debug("queryModulars")
    return HttpResponse("modularsStr")

class QueryStatisticsAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        # .Device.objects.all()
        from django.db import connection, connections
        dataDict = {}
        total = sqlFetchone("select count(1) from device_device")
        dataDict.setdefault("total",total[0])
        online = sqlFetchone("select count(1) from device_device where online=1")
        dataDict.setdefault("online",online[0])
        dataDict.setdefault("fault",0)
        logging.debug((dataDict))
        return JsonResponse(dataDict)

class QueryDeviceAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request):
        logger.debug(request.GET)
        return JsonResponse(request.GET)
        # product = request.POST.get("products")