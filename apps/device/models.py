from django.db import models
from datetime import datetime
# Create your models here.

class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
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
    ifArgsSet = (
        (0,'失败'),
        (1,'成功'),
        (2,'未知'),
    )
    dev_states = (
        (0,"出厂"),
        (1,"正常制水"),
        (2,"冲洗"),
        (3,"水满"),
        (4,"缺水"),
        (5,"臭氧"),
        (6,"清洗前置罐"),
        (10,"参数设置失败"),
        (11,"正常制水_repeat"),
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
    nid = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=50, verbose_name='设备ID',help_text="设备ID")
    remarks = models.CharField(max_length=50, verbose_name='备注名称',blank=True,null=True,help_text="备注名称")
    online = models.IntegerField(verbose_name='是否离线',choices=lineStates,default=2,help_text="是否离线")
    arg_set_state = models.IntegerField(verbose_name='参数设置是否成功',choices=ifArgsSet,default=2,help_text="参数设置是否成功")
    temperature = models.FloatField(max_length=10, verbose_name='温度',blank=True,null=True,help_text="温度")
    signal = models.FloatField(max_length=10, verbose_name='信号',blank=True,null=True,help_text="信号")
    chunShui = models.IntegerField(verbose_name='纯水',default=0,help_text="纯水")
    yuanShui = models.IntegerField(verbose_name='原水',default=0,help_text="原水")
    zhiShuiTime = models.IntegerField(verbose_name='制水时间',default=0,help_text="制水时间")  #单位 分钟
    zhiShuiTotalTime = models.IntegerField(verbose_name='制水累计',default=0,help_text="制水累计")  #单位 天
    MainboardID = models.CharField(max_length=50, verbose_name='主板编号',help_text="主板编号")
        
    wenKongSwitch = models.BooleanField(verbose_name='温控开关',default=False)
    dev_state = models.IntegerField(verbose_name='设备状态',choices=dev_states,blank=True,null=True)
    yuanShuibeng = models.BooleanField(verbose_name='原水泵',default=False)
    jinShuiFa = models.BooleanField(verbose_name='进水阀',default=False)
    diyaSwitch = models.BooleanField(verbose_name='低压开关',default=False)
    gaoYaBeng = models.BooleanField(verbose_name='高压泵',default=False)
    chongxiFa = models.BooleanField(verbose_name='冲洗阀',default=False)
    chouYangQi = models.BooleanField(verbose_name='臭氧器',default=False)
    remoteSwitch = models.BooleanField(verbose_name='远程开关',default=False)

    _1t = models.IntegerField(verbose_name='开启冲洗阀时间1T(1-240秒)',blank=True,null=True)
    _2t = models.IntegerField(verbose_name='开启制水泵时间2T(1-240秒)',blank=True,null=True)
    _3t = models.IntegerField(verbose_name='循环冲洗时间3T(1-240秒)',blank=True,null=True)
    _4t = models.IntegerField(verbose_name='水满后冲洗时间4T(1-240秒)',blank=True,null=True)
    _5t = models.IntegerField(verbose_name='冲洗时间间隔5T(1-240分)',blank=True,null=True)
    _6t = models.IntegerField(verbose_name='水满制水泵停止时间6T(5-240秒)',blank=True,null=True)
    _7t = models.IntegerField(verbose_name='臭氧杀菌时间7T(5-240秒)',blank=True,null=True)
    _8t = models.IntegerField(verbose_name='臭氧杀菌间隔8T(10-240分)',blank=True,null=True)
    _1c = models.IntegerField(verbose_name='温控加热启动温度1C(1-30℃)',blank=True,null=True)
    _2c = models.IntegerField(verbose_name='温控加热停止温度2C(1-30℃)',blank=True,null=True)
    _2d = models.IntegerField(verbose_name='电导率显示方式2D(1TDS 2电导率)',blank=True,null=True)
    _3d = models.IntegerField(verbose_name='TDS修正数据3D(0-255)',blank=True,null=True)
    _4d = models.IntegerField(verbose_name='洗膜方式4D(1低压 2高压)',blank=True,null=True)

   
    def __str__(self):
        return self.device_id

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'   
        indexes = [models.Index(fields=['online',"dev_state"]),]

class RepairDevice(models.Model):
    """
    主页->报修管理 页面里展示数据
    """
    ifSolve = ((1,"已解决"),(2,"未解决"))
    ifSatisfied = (
        (1,"非常满意"),
        (2,"满意"),
        (3,"不满意"),
        (4,"非常不满意"),
    )
    repairID = models.CharField(max_length=20, verbose_name='报修编号') #设备号-序号
    repair = models.CharField(max_length=20, verbose_name='报修状态',blank=True,null=True)
    reportMan = models.CharField(max_length=20, verbose_name='报修人员',blank=True,null=True)
    Phone = models.CharField(max_length=20, verbose_name='联系电话',blank=True,null=True)
    # dev_state = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True,verbose_name='设备号') #一对多关系
    dev_state = models.CharField(max_length=40,verbose_name='设备号') #一对多关系
    repairAddr = models.CharField(max_length=20, verbose_name='维修地点',blank=True,null=True)
    descErorr = models.CharField(max_length=20, verbose_name='故障简述',blank=True,null=True)
    runErrorTime = models.DateTimeField(verbose_name='故障日期')
    repairMan = models.CharField(max_length=20, verbose_name='上门维修人员',blank=True,null=True)
    repairManPhone = models.CharField(max_length=20, verbose_name='维修人员电话',blank=True,null=True)

    ifOk = models.IntegerField(verbose_name='是否解决',choices=ifSolve,blank=True,null=True)
    ifSatisfied = models.IntegerField(verbose_name='是否满意',choices=ifSatisfied,blank=True,null=True)
    comment = models.CharField(max_length=400, verbose_name='评价',blank=True,null=True)

    def __str__(self):
        return self.repairID

    class Meta:
        verbose_name = '报修单展示'
        verbose_name_plural = verbose_name

class RepairDeviceAdd(models.Model):
    """
    主页->报修管理-> 一键报修 页面里展示数据
    """
    ifSolve = ((1,"已解决"),(2,"未解决"))
    ifSatisfied = (
        (1,"非常满意"),
        (2,"满意"),
        (3,"不满意"),
        (4,"非常不满意"),
    )
    deviceID = models.CharField(max_length=20, verbose_name='设备号')
    reportMan = models.CharField(max_length=20, verbose_name='报修人员名称',blank=True,null=True)
    Phone = models.CharField(max_length=20, verbose_name='电话',blank=True,null=True)
    repairProf = models.CharField(max_length=20, verbose_name='报修内容描述',blank=True,null=True)
    repairAddr = models.CharField(max_length=20, verbose_name='报修地址',blank=True,null=True)

    def __str__(self):
        return self.deviceID

    class Meta:
        verbose_name = '报修单添加'
        verbose_name_plural = verbose_name


class AfterSaleManage(BaseModel):
    """
    主页->售后管理 页面里展示数据
    """
    notifyID = models.CharField(max_length=40, verbose_name='提醒编号')   #设备号-序号
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

    def __str__(self):
        return self.notifyID

    class Meta:
        verbose_name = '售后提醒单'
        verbose_name_plural = '售后提醒单'


class AfterSaleManageSet(BaseModel):
    """
    主页->售后管理->设置 页面里展示数据
    """

    deviceID = models.ForeignKey(Device, on_delete=models.SET_NULL,verbose_name='设备号',null=True)
    SGName = models.CharField(max_length=40, verbose_name='砂罐名称')
    SGUseTime = models.DateTimeField(max_length=40, verbose_name='砂罐使用时间')
    SGSetCycle = models.IntegerField(verbose_name='砂罐设置周期')

    TGName = models.CharField(max_length=40, verbose_name='碳罐名称')
    TGUseTime = models.DateTimeField(max_length=40, verbose_name='碳罐使用时间')
    TGSetCycle = models.IntegerField(verbose_name='碳罐设置周期')

    RHName = models.CharField(max_length=40, verbose_name='软化名称')
    RHUseTime = models.DateTimeField(max_length=40, verbose_name='软化使用时间')
    RHSetCycle = models.IntegerField(verbose_name='软化设置周期')

    JLName = models.CharField(max_length=40, verbose_name='精滤名称')
    JLUseTime = models.DateTimeField(max_length=40, verbose_name='精滤使用时间')
    JLSetCycle = models.IntegerField(verbose_name='精滤设置周期')

    ROName = models.CharField(max_length=40, verbose_name='RO膜名称')
    ROUseTime = models.DateTimeField(max_length=40, verbose_name='RO膜使用时间')
    ROSetCycle = models.IntegerField(verbose_name='RO膜设置周期')

    def __str__(self):
        return self.deviceID

    class Meta:
        verbose_name = '售后提醒单添加'
        verbose_name_plural = verbose_name