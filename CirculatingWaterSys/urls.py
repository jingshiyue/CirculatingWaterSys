"""CirculatingWaterSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from device.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static 

router = DefaultRouter()  #建议不用这个，会暴露很多接口出去
router.register('deviceEdit', DeviceEditViewset,basename='deviceEdit')
router.register('deviceQuery', DeviceQueryViewSet,basename='deviceQuery')
router.register('RepairDeviceViewset', RepairDeviceViewset,basename='RepairDeviceViewset')
router.register('afterSaleManageViewset', AfterSaleManageViewset,basename='AfterSaleManageViewset')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/',include_docs_urls(title='水处理智能控制系统')),
    # path('api-auth/',include('rest_framework.urls')),
    path('jwt_auth/', obtain_jwt_token ),
    path('index/index/login/', TemplateView.as_view(template_name='device/index/index/login.html'),name='login'), #linux里路径必须是/ 分隔
    path('index/index.html/', TemplateView.as_view(template_name='device/index/index/index.html'),name='index'),   #需要加认证
    path('index/index/my.html/', TemplateView.as_view(template_name='device/index/index/my.html'),name='my'), 
    path('index/Equipment/index.html/', TemplateView.as_view(template_name='device/index/Equipment/index.html')), 
    re_path('index/Equipment/pclist.html/?maxDeviceID=3999999&page=1', TemplateView.as_view(template_name='device/index/Equipment/index.html')),   #大屏展示
    re_path('index/setting/sell/Id/paramset/(?P<device_id>\S+)/',ParamSetAPIView.as_view()),                                                                                 
    re_path('index/Equipment/statetu/Id/runstatus/(?P<device_id>\S+)/',RunStatusAPIView.as_view()),                                                                                 
    path('index/repairs/index.html/', TemplateView.as_view(template_name='device/index/repairs/index.html')),
    path('index/repairs/add.html/', TemplateView.as_view(template_name='device/index/repairs/add.html')), 
    re_path('index/repairs/addfeedback/(?P<repairID>\S+)/', AddFeedbackAPIView.as_view()),
    
    path('index/remind/index.html/',TemplateView.as_view(template_name='device/index/remind/index.html')), 
    path('index/remind/add.html/',AddAfterSaleAPIView.as_view()), #TemplateView.as_view(template_name='device/index/remind/add.html')
    path('index/fault/index.html/', TemplateView.as_view(template_name='device/index/fault/index.html')), 

    path('index/index/login.html/', TemplateView.as_view(template_name='device/index/index/login.html')),
    path('index/user/changePwd.html/',ChangePwdAPIView.as_view()),
    path('index/index/logout.html/', TemplateView.as_view(template_name='device/index/index/logout.html')),

    path('queryStatistics/',QueryStatisticsAPIView.as_view()),
    path('queryDeviceAPIView/',QueryDeviceAPIView.as_view()),
    # path('get_user/',get_user),
    re_path('^', include(router.urls)),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

# url(r"bookset/$",views.BookSet.as_view({'get': 'list', 'post': 'create'})),
# url(r"bookset/(?P<pk>\d+)/$",views.BookSet.as_view({'get': 'retrieve', 'put': 'update','delete': 'destroy'})),


# path('index/', DeviceViewset.as_view() ),  as_view({'get': 'list'})