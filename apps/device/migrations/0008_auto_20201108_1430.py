# Generated by Django 2.2 on 2020-11-08 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0007_auto_20201108_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='deviceArgs',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='device.Device_args_set', verbose_name='设备参数'),
        ),
        migrations.AlterField(
            model_name='device',
            name='deviceState',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='device.Device_run_state', verbose_name='设备状态'),
        ),
        migrations.AlterField(
            model_name='device_run_state',
            name='dev_state',
            field=models.IntegerField(choices=[(0, '出厂'), (1, '正常制水'), (2, '冲洗'), (3, '水满'), (4, '缺水'), (5, '臭氧'), (6, '清洗前置罐'), (10, '参数设置失败'), (11, '正常制水?重复'), (12, '冲洗'), (13, '水满'), (14, '缺水'), (15, '臭氧'), (16, '清洗前置罐'), (20, '无原水'), (21, '低压'), (30, '无原水'), (31, '低压')], default=False, verbose_name='设备状态'),
        ),
    ]
