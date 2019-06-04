# Generated by Django 2.2 on 2019-06-04 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thermostat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thermostat_state', models.BooleanField(default=False, verbose_name='Стан термостату')),
                ('current_state', models.CharField(max_length=20, verbose_name='Стан термостату')),
                ('temp', models.FloatField(default=0, verbose_name='Температура')),
                ('set_temp', models.FloatField(default=0, verbose_name='Встановлена температура')),
                ('co2', models.FloatField(blank=True, null=True, verbose_name='Рівень CO2')),
                ('set_co2', models.FloatField(blank=True, null=True, verbose_name='Встановлений рівень CO2')),
                ('light', models.BooleanField(default=False, verbose_name='Стан освітлення')),
                ('light_R', models.IntegerField(default=0, verbose_name='R')),
                ('light_G', models.IntegerField(default=0, verbose_name='G')),
                ('light_B', models.IntegerField(default=0, verbose_name='B')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, max_length=1000, null=True)),
                ('is_private', models.BooleanField(default=False)),
                ('last_use', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_name', models.CharField(blank=True, max_length=100, null=True)),
                ('thermostat_state', models.BooleanField(default=False, verbose_name='Стан термостату')),
                ('set_temp', models.FloatField(default=0, verbose_name='Встановити температуру')),
                ('set_co2', models.FloatField(blank=True, null=True, verbose_name='Встановити рівень CO2')),
                ('light', models.BooleanField(default=False, verbose_name='Стан освітлення')),
                ('light_R', models.IntegerField(default=0, verbose_name='R')),
                ('light_G', models.IntegerField(default=0, verbose_name='G')),
                ('light_B', models.IntegerField(default=0, verbose_name='B')),
                ('duration_d', models.IntegerField(default=0, verbose_name='Тривалість, дні')),
                ('duration_h', models.IntegerField(default=0, verbose_name='Тривалість, години')),
                ('duration_m', models.IntegerField(default=0, verbose_name='Тривалість, хвилини')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ts.Program')),
            ],
        ),
        migrations.CreateModel(
            name='LogUseProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ts.Program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
