from django.contrib import admin
from django.db import models
from datetime import datetime

# Register your models here.

class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='创建人')
    class Meta:
        abstract = True

class Device(BaseModel):
    """
    主页->设备管理 页面里展示数据
    设备模型
    """
    lineStates = (
        (0, '离线'),
        (1, '在线'),
        (2, '未知'),
    )
    device_id = models.CharField(max_length=50, verbose_name='设备ID')
    remarks = models.CharField(max_length=50, verbose_name='备注名称',blank=True)
    online = models.IntegerField(verbose_name='是否离线',choices=lineStates,default=2)
    arg_set_state = models.CharField(max_length=50, verbose_name='参数设置',blank=True)
    temperature = models.FloatField(max_length=10, verbose_name='温度',blank=True)
    signal = models.FloatField(max_length=10, verbose_name='信号',blank=True)
    chunShui = models.IntegerField(verbose_name='纯水')
    yuanShui = models.IntegerField(verbose_name='原水')
    zhiShuiTime = models.IntegerField(verbose_name='制水时间')  #单位 分钟
    zhiShuiTotalTime = models.IntegerField(verbose_name='制水累计')  #单位 天
   
    def __str__(self):
        return self.device_id

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'

class Device_args_set(models.Model):
    """
    反渗透设备参数设置 页面
    """
    device_id = models.ForeignKey(Device, on_delete=models.SET_NULL,verbose_name='设备ID')
    _1t = models.IntegerField(max_length=6, verbose_name='开启冲洗阀时间1T(1-240秒)')
    _2t = models.IntegerField(max_length=6, verbose_name='开启制水泵时间2T(1-240秒)')
    _3t = models.IntegerField(max_length=6, verbose_name='循环冲洗时间3T(1-240秒)')
    _4t = models.IntegerField(max_length=6, verbose_name='水满后冲洗时间4T(1-240秒)')
    _5t = models.IntegerField(max_length=6, verbose_name='冲洗时间间隔5T(1-240分)')
    _6t = models.IntegerField(max_length=6, verbose_name='水满制水泵停止时间6T(5-240秒)')
    _7t = models.IntegerField(max_length=6, verbose_name='臭氧杀菌时间7T(5-240秒)')
    _8t = models.IntegerField(max_length=6, verbose_name='臭氧杀菌间隔8T(10-240分)')
    _1c = models.IntegerField(max_length=6, verbose_name='温控加热启动温度1C(1-30℃)')
    _2c = models.IntegerField(max_length=6, verbose_name='温控加热停止温度2C(1-30℃)')
    _2d = models.IntegerField(max_length=1, verbose_name='电导率显示方式2D(1TDS 2电导率)')
    _3d = models.IntegerField(max_length=6, verbose_name='TDS修正数据3D(0-255)')
    _4d = models.IntegerField(max_length=1, verbose_name='洗膜方式4D(1低压 2高压)')

    
class Device_run_state(models.Model):
    """
    设备运行状态 页面
    """

    dev_states = (
        (0,"出厂"),
        (1,"正常制水"),
        (2,"冲洗"),
        (3,"水满"),
        (4,"缺水"),
        (5,"臭氧"),
        (6,"清洗前置罐"),
        (10,"参数设置失败"),
        (11,"正常制水"),
        (12,"冲洗"),
        (13,"水满"),
        (14,"缺水"),
        (15,"臭氧"),
        (16,"清洗前置罐"),
        (20,"无原水"),
        (21,"低压"),
        (30,"无原水"),
        (31,"低压"),
    )
    
    device_id = models.ForeignKey(Device, on_delete=models.SET_NULL,verbose_name='设备ID')
    wenKongSwitch = models.IntegerField(max_length=1, verbose_name='温控开关')
    dev_state = models.CharField(max_length=2, verbose_name='设备状态',choices=dev_states)

    yuanShuibeng = models.IntegerField(max_length=1, verbose_name='原水泵')
    jinShuiFa = models.IntegerField(max_length=1, verbose_name='进水阀')
    diyaSwitch = models.IntegerField(max_length=1, verbose_name='低压开关')
    gaoYaBeng = models.IntegerField(max_length=1, verbose_name='高压泵')
    chongxiFa = models.IntegerField(max_length=1, verbose_name='冲洗阀')
    chouYangQi = models.IntegerField(max_length=1, verbose_name='臭氧器')
    remoteSwitch = models.IntegerField(max_length=1, verbose_name='远程开关')


class RepairDevice(BaseModel):
    """
    主页->报修管理 页面里展示数据
    """
    repairID = models.CharField(max_length=20, verbose_name='报修编号') #与设备号有关系
    repair = models.CharField(max_length=20, verbose_name='报修状态')
    reportMan = models.CharField(max_length=20, verbose_name='报修人员')
    Phone = models.CharField(max_length=20, verbose_name='联系电话')
    dev_state = models.CharField(max_length=20, verbose_name='设备号')  
    repairAddr = models.CharField(max_length=20, verbose_name='维修地点')
    descErorr = models.CharField(max_length=20, verbose_name='故障简述')
    runErrorTime = models.DateField(verbose_name='故障日期')
    repairMan = models.CharField(max_length=20, verbose_name='上门维修人员')
    repairManPhone = models.CharField(max_length=20, verbose_name='维修人员电话')
    ifOk = models.IntegerField(verbose_name='是否解决')
    ifSatisfied = models.IntegerField(verbose_name='是否满意')
    comment = models.CharField(max_length=400, verbose_name='评价',blank=True)


class AfterSaleManage(BaseModel):
    """
    主页->售后管理 页面里展示数据
    """
    notifyID = models.CharField(max_length=40, verbose_name='提醒编号')
    SGName = models.CharField(max_length=20, verbose_name='砂罐名称')
    SGcycleTime = models.IntegerField(verbose_name='砂罐周期')
    SGprotectTime = models.DateField(verbose_name='砂罐保养开始时间')

    TGName = models.CharField(max_length=20, verbose_name='碳罐名称')
    TGcycleTime = models.IntegerField(verbose_name='碳罐周期')
    TGprotectTime = models.DateField(verbose_name='碳罐保养开始时间')

    RHName = models.CharField(max_length=20, verbose_name='软化名称')
    RHcycleTime = models.IntegerField(verbose_name='软化周期')
    RHprotectTime = models.DateField(verbose_name='软化保养开始时间')

    JLName = models.CharField(max_length=20, verbose_name='精滤名称')
    JLcycleTime = models.IntegerField(verbose_name='精滤周期')
    JLprotectTime = models.DateField(verbose_name='精滤保养开始时间')
    
    ROName = models.CharField(max_length=20, verbose_name='RO膜名称')
    ROcycleTime = models.IntegerField(verbose_name='RO膜周期')
    ROprotectTime = models.DateField(verbose_name='RO膜保养开始时间')