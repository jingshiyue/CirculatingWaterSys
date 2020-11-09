from rest_framework import serializers
from .models import *
import logging
logger = logging.getLogger(__name__)

class Device_run_stateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device_run_state
        fields = '__all__'

class RepairDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    device_run_state = Device_run_stateSerializer()
    # device_run_state = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = Device
        fields = '__all__'
        # depth = 2

    def create(self, validated_data):
        device_run_state_obj =validated_data.pop('device_run_state')
        logger.debug(device_run_state_obj)
        # Device_run_state.objects.create(**device_run_state_obj)
        instance = Device.objects.create(**validated_data)
        return instance

    # def get_device_run_state(self, obj):
    #     logger.debug(1111111111)
    #     logger.debug(obj)
    #     return Device_run_stateSerializer(obj.device_run_state.all())

    def update(self, instance, validated_data):
        device_run_state = validated_data.pop('device_run_state')
        deviceID = validated_data.get("device_id",None)
        obj = Device.objects.get(device_id=deviceID)

        deviceID = validated_data.get("device_id",None)
        Device.objects.get(device_id=deviceID )

        instance = super(DeviceSerializer, self, ).update(instance, validated_data)
        return instance


    # def to_representation(self, instance):
    #     representation = super(EquipmentSerializer, self).to_representation(instance)
    #     representation['assigment'] = AssignmentSerializer(instance.assigment_set.all(), many=True).data
    #     return representation 


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

