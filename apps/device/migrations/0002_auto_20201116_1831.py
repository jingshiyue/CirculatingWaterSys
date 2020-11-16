# Generated by Django 2.2 on 2020-11-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repairdevice',
            options={'verbose_name': '报修单', 'verbose_name_plural': '报修单'},
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.CharField(help_text='设备ID', max_length=50, unique=True, verbose_name='设备ID'),
        ),
    ]