# Generated by Django 2.2 on 2019-06-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0003_auto_20190604_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='co2_control',
            field=models.BooleanField(default=False, verbose_name='Увімкнути контроль СО2'),
        ),
        migrations.AddField(
            model_name='thermostat',
            name='co2_control',
            field=models.BooleanField(default=False, verbose_name='Стан контролю СО2'),
        ),
    ]
