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

router = DefaultRouter()
router.register('deviceEdit', DeviceEditViewset,basename='device')
router.register('deviceQuery', DeviceQueryViewSet,basename='device')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/',include_docs_urls(title='水处理智能控制系统')),
    # path('api-auth/',include('rest_framework.urls')),
    path('jwt_auth/', obtain_jwt_token ),
    path('queryModulars/', queryModulars ),
    path('index/index/login/', TemplateView.as_view(template_name='device/index/index/login.html'),name='login'), #linux里路径必须是/ 分隔
    path('index/index.html/', TemplateView.as_view(template_name='device/index/index/index.html'),name='index'),   #需要加认证
    path('index/index/my.html/', TemplateView.as_view(template_name='device/index/index/my.html'),name='my'), 
    path('index/Equipment/index.html/', TemplateView.as_view(template_name='device/index/Equipment/index.html')), 


    re_path('^', include(router.urls)),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)



# path('index/', DeviceViewset.as_view() ),  as_view({'get': 'list'})