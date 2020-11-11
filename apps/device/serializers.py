from rest_framework import serializers
from .models import *
import logging
logger = logging.getLogger(__name__)

# class Device(serializers.ModelSerializer):
#     device_id_id = serializers.CharField(max_length=200)
#     class Meta:
#         model = Device_run_state
#         fields = '__all__'

class RepairDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    # device_run_state = Device_run_stateSerializer()
    class Meta:
        model = Device
        fields = '__all__'
        # depth = 2

    # def create(self, validated_data):
    #     device_run_state_obj =validated_data.pop('device_run_state')
    #     device = Device.objects.create(**validated_data)
    #     Device_run_state.objects.create(device_id=device,**device_run_state_obj)
    #     return device

    # def update(self, instance, validated_data):
    #     deviceRunStateData = validated_data.pop('device_run_state')
    #     instance.__dict__.update(**validated_data)
    #     deviceRunState = instance.device_run_state
    #     logger.debug(deviceRunStateData)
    #     deviceRunState.__dict__.update(**deviceRunStateData)
    #     return instance


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

