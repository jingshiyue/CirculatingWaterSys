from django.contrib import admin
from device.models import *

# Register your models here.


class DeviceAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ('device_id','remarks',)


class Device_args_setAdmin(admin.ModelAdmin):
    list_per_page = 20


class Device_run_stateAdmin(admin.ModelAdmin):
    list_per_page = 20
    
class RepairDeviceAdmin(admin.ModelAdmin):
    list_per_page = 20


admin.site.register(Device,DeviceAdmin)
admin.site.register(Device_args_set,Device_args_setAdmin)
admin.site.register(Device_run_state,Device_run_stateAdmin)
admin.site.register(RepairDevice,RepairDeviceAdmin)

