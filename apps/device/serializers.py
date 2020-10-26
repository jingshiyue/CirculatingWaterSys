from rest_framework import serializers
from .models import *

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class Device_args_setSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device_args_set
        fields = '__all__'

class Device_run_stateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device_run_state
        fields = '__all__'

class RepairDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class RepairDeviceAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairDeviceAdd
        fields = '__all__'

class AfterSaleManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfterSaleManage
        fields = '__all__'

class AfterSaleManageSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfterSaleManageSet
        fields = '__all__'