from django.db import connection, connections
import os,django,sys
sys.path.append(sys.path[0]+"\\..")
print(sys.path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CirculatingWaterSys.settings')
django.setup()
from device.models import *


def sqlFetchone(sql):
    # 返回tuple, (21,)
    cursor = connection.cursor()
    cursor.execute(sql)
    rst = cursor.fetchone()
    cursor.close()
    return rst 

def sqlFetchall(sql):
    # 返回tuple, ((21,),)
    cursor = connection.cursor()
    cursor.execute(sql)
    rst = cursor.fetchall()
    cursor.close()
    return rst 


if __name__ == "__main__":
    for i in range(1001,1043):
        validated_data = {}
        validated_data.setdefault("device_id",str(i))
        validated_data.setdefault("MainboardID",str(i)+"-编号")
        validated_data.setdefault("remarks",str(i)+"-备注")
        Device.objects.create(**validated_data)
        print(f"add Device {i} suc ..")