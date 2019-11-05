from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Thermostat(models.Model):
    thermostat_state = models.BooleanField("Стан термостату", default=False)
    current_state = models.CharField("Стан термостату", max_length=20)

    temp = models.FloatField("Температура", default=0)
    set_temp = models.FloatField("Встановлена температура", default=0)

    co2_control = models.BooleanField("Стан контролю СО2", default=False)
    co2 = models.FloatField("Рівень CO2", blank=True, null=True)
    set_co2 = models.FloatField("Встановлений рівень CO2", blank=True, null=True)

    light = models.IntegerField("Стан освітлення", default=0)

    light_UV = models.IntegerField("UV", default=0)
    light_R = models.IntegerField("R", default=0)
    light_G = models.IntegerField("G", default=0)
    light_B = models.IntegerField("B", default=0)

    time = models.DateTimeField(auto_now_add=True)

    def get_light_mode(self):
        if self.light == 1:
            return "UV"
        elif self.light == 2:
            return "RGB"
        elif self.light == 3:
            return "RGB & UV"
        return "Off"

    def __str__(self):
        return f"{self.time.strftime('%Y-%m-%d %H:%M:%S')} | State: {'On' if self.thermostat_state else 'Off'} | t: {self.temp}" \
               f" | light: {self.get_light_mode()}"


class Program(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    last_use = models.DateTimeField(blank=True, null=True)
    looping = models.IntegerField("Кількість зациклень", default=1)

    def __str__(self):
        return f"Program: {self.name}"


class Phase(models.Model):
    program = models.ForeignKey(Program, blank=True, null=True, on_delete=models.CASCADE)
    phase_name = models.CharField(max_length=100, blank=True, null=True)
    thermostat_state = models.BooleanField("Стан термостату", default=False)
    set_temp = models.IntegerField("Встановити температуру", default=0)

    co2_control = models.BooleanField("Увімкнути контроль СО2", default=False)
    set_co2 = models.IntegerField("Встановити рівень CO2", default=0)

    light = models.IntegerField("Стан освітлення", default=0)

    light_UV = models.IntegerField("UV", default=0)
    light_R = models.IntegerField("R", default=0)
    light_G = models.IntegerField("G", default=0)
    light_B = models.IntegerField("B", default=0)

    duration_d = models.IntegerField("Тривалість, дні", default=0)
    duration_h = models.IntegerField("Тривалість, години", default=0)
    duration_m = models.IntegerField("Тривалість, хвилини", default=0)

    order_execution = models.IntegerField("Порядок виконання", blank=True, null=True)

    def __str__(self):
        return f"Program: {self.program} | Phase: {self.phase_name}"


class LogUseProgram(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)