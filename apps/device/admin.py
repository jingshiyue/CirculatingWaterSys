from django.contrib import admin
from device.models import *

# Register your models here.


class DeviceAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ('device_id','remarks',)

    
class RepairDeviceAddAdmin(admin.ModelAdmin):
    list_per_page = 20

class AfterSaleManageSetAdmin(admin.ModelAdmin):
    list_per_page = 20



admin.site.register(Device,DeviceAdmin)
admin.site.register(RepairDeviceAdd,RepairDeviceAddAdmin)
admin.site.register(AfterSaleManageSet,AfterSaleManageSetAdmin)


